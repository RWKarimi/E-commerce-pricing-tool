from pydantic import BaseModel
from typing import List, Optional

class Deal(BaseModel):
    key: str
    main_category: str
    current_price: float
    median_price: float
    price_to_cat_median: float
    title: Optional[str] = None
    url: Optional[str] = None

class PagedDeals(BaseModel):
    items: List[Deal]
    total: int
    page: int
    page_size: int
