# jumia_scraper.py
# ---------------------------------------------------
# Scraping product data from Jumia Kenya
# ---------------------------------------------------

import os
import csv
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# --- Basic setup ---
headers = {"User-Agent": "Mozilla/5.0"}
os.makedirs("Data", exist_ok=True)
CSV_PATH = "Data/Shorten_Scraped_Data.csv"
MAX_PAGES = 1  # You can increase this for more pages


# --- Helper function to scrape product details ---
def get_product_details(product_url):
    """Scrape additional details from a product page"""
    try:
        res = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(res.text, "lxml")

        title = soup.find("h1", class_="-fs20")
        brand = soup.find("a", class_="_more")
        orig_price = soup.find("span", class_="-lthr")
        discount = soup.find("span", class_="bdg _dsct _dyn -mls")
        verified_ratings = soup.find("a", class_="-plxs")
        stars = soup.find("div", class_="stars")
        seller = soup.find("p", class_="-m -pbs")
        category = soup.find("a", class_="cbs")

        return {
            "title": title.text.strip() if title else None,
            "brand": brand.text.strip() if brand else None,
            "original_price": orig_price.text.strip() if orig_price else None,
            "discount": discount.text.strip() if discount else None,
            "verified_ratings": verified_ratings.text.strip() if verified_ratings else None,
            "rating_number": stars.text.strip() if stars else None,
            "seller": seller.text.strip() if seller else None,
            "main_category": category.text.strip() if category else None
        }

    except Exception as e:
        print("Error getting product details:", e)
        return {}


# --- Function to scrape one listing page ---
def scrape_page(page_num):
    """Scrape all products from a single Jumia page"""
    print(f"Scraping page {page_num}...")
    url = f"https://www.jumia.co.ke/catalog/?page={page_num}"
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print("Failed to load page", page_num)
        return []

    soup = BeautifulSoup(res.text, "lxml")
    products = soup.find_all("article", class_="prd")

    all_items = []
    for p in products:
        link = p.find("a", class_="core")
        if not link:
            continue

        product_url = "https://www.jumia.co.ke" + link["href"]
        img_tag = p.find("img", class_="img")
        price_tag = p.find("div", class_="prc")

        image = img_tag.get("data-src") or img_tag.get("src") if img_tag else None
        current_price = price_tag.text.strip() if price_tag else None

        details = get_product_details(product_url)

        product = {
            "date_scraped": datetime.today().strftime("%Y-%m-%d"),
            "page_number": page_num,
            "product_url": product_url,
            "image": image,
            "current_price": current_price,
            **details
        }

        all_items.append(product)
        print("Scraped:", details.get("title"))
        time.sleep(random.uniform(2, 5))  # polite delay between requests

    return all_items


# --- Resume logic ---
def get_resume_page():
    """Resume from last scraped page if CSV exists"""
    if not os.path.exists(CSV_PATH):
        return 1

    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        done_pages = {int(row["page_number"]) for row in reader if row.get("page_number")}
        if done_pages:
            return max(done_pages) + 1
    return 1


# --- Main script ---
def main():
    start_page = get_resume_page()
    fieldnames = [
        "date_scraped", "page_number", "product_url", "image", "current_price",
        "title", "brand", "original_price", "discount",
        "verified_ratings", "rating_number", "seller", "main_category"
    ]

    file_exists = os.path.exists(CSV_PATH)

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        for page in range(start_page, MAX_PAGES + 1):
            data = scrape_page(page)
            for item in data:
                writer.writerow(item)
            print("Finished page", page)
            time.sleep(random.uniform(5, 10))  # wait between pages

    print("Scraping complete!")


# --- Run the script ---
if __name__ == "__main__":
    main()
