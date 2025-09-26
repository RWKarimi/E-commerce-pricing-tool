from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Optional
from pathlib import Path
import pandas as pd
import time

from settings import settings
from models import PagedDeals

app = FastAPI(title="Price Landscape API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.ALLOW_ORIGINS.split(",")],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

_cache = {}
def cached_read_csv(name: str) -> pd.DataFrame:
    p = settings.OUT_DIR / name
    if not p.exists(): raise FileNotFoundError(name)
    key = (name, p.stat().st_mtime); now = time.time()
    hit = _cache.get(key)
    if hit and now - hit["ts"] < settings.CACHE_SEC: return hit["df"]
    df = pd.read_csv(p); _cache.clear(); _cache[key] = {"df": df, "ts": now}
    return df

@app.get("/health")
def health(): return {"ok": True}

@app.get("/analytics/medians")
def medians(limit: int = 50):
    df = cached_read_csv("median_price_by_category.csv").head(limit)
    return JSONResponse(df.to_dict(orient="records"))

@app.get("/analytics/medians/weekly")
def medians_week(category: Optional[str] = None, limit: int = 500):
    df = cached_read_csv("median_price_by_category__weekly.csv")
    if category: df = df[df["_main_category"] == category]
    df = df.sort_values(["_main_category", "week"]).head(limit)
    return JSONResponse(df.to_dict(orient="records"))

@app.get("/analytics/watchlist", response_model=PagedDeals)
def watchlist(page: int = 1, page_size: int = 25, threshold: float = 0.90, category: Optional[str] = None):
    try:
        df = cached_read_csv("watchlist_top50_overall.csv")
    except FileNotFoundError:
        feat = cached_read_csv("price_quantile_features.csv")
        df = feat[feat["price_to_cat_median"] <= threshold].copy()
    for col in ["current_price","median_price","price_to_cat_median","main_category"]:
        if col not in df.columns: raise HTTPException(500, f"Missing column: {col}")
    if category: df = df[df["main_category"] == category]
    df = df.sort_values("price_to_cat_median"); total = len(df)
    start = (page-1)*page_size; end = start + page_size
    page_df = df.iloc[start:end].copy()
    if "key" not in page_df.columns: page_df["key"] = page_df.index.astype(str)
    cols = ["key","main_category","current_price","median_price","price_to_cat_median"]
    for c in ["title","url"]:
        if c in page_df.columns: cols.append(c)
    return {"items": page_df[cols].to_dict("records"), "total": total, "page": page, "page_size": page_size}
