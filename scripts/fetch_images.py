#!/usr/bin/env python3
"""
Fetch official, crisp product images for curated budget watches using Brave Search Images API.
Saves them locally to assets/images/<id>.jpg
"""
import os
import sys
import json
import time
import requests
from PIL import Image
import io

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, "assets", "images")
os.makedirs(IMG_DIR, exist_ok=True)

API_KEY = os.environ.get("BRAVE_SEARCH_API_KEY")
if not API_KEY:
    print("Error: BRAVE_SEARCH_API_KEY not found in environment.")
    sys.exit(1)

SEARCH_QUERIES = {
    "addiesdive-ad2030": "Addiesdive AD2030 sand wave textured dial watch product",
    "steeldive-sd1970": "Steeldive SD1970 Captain Willard automatic dive watch product",
    "steeldive-sd1953": "Steeldive SD1953 Submariner automatic dive watch black ceramic",
    "escapement-time-35mm-ks": "Escapement Time 35mm King Elegance quartz dress watch white dial",
    "berny-t2566m-titanium": "Berny T2566M Titanium field watch sweeping quartz product",
    "militado-ml05-field": "Militado ML05 Dirty Dozen military field watch black dial",
    "pagani-design-pd1701": "Pagani Design PD-1701 Speedmaster chronograph watch product black",
    "pagani-design-pd1644": "Pagani Design PD-1644 Daytona racing chronograph watch white dial",
    "tandorio-36mm-flieger": "Tandorio 36mm pilot flieger automatic watch sterile dial",
    "tandorio-37mm-skx013": "Tandorio 37mm SKX013 automatic dive watch jubilee",
    "sanda-1108-tank": "Sanda 1108 Tank rectangular vintage quartz watch leather",
    "casio-duro-mdv107": "Casio Duro MDV-107 diver watch black dial resin strap",
    "casio-a168wa": "Casio A168WA 1YES vintage digital stainless steel watch illuminator",
    "casio-ltp-v007l": "Casio LTP-V007L rectangular mini tank dress watch leather",
    "burei-classic-date": "Burei minimalist sapphire quartz watch date leather",
    "merkur-pierre-paulin-sector": "Pierre Paulin Merkur vintage sector dial salmon copper watch",
    "sugess-celestial-heritage": "Sugess Moonphase Master Seagull ST2528 automatic watch blue",
    "lige-8936-racing-chrono": "Lige 8936 racing chronograph watch silicone strap",
    "addiesdive-ad2023-explorer": "Addiesdive AD2023 Explorer 36mm sweeping quartz watch black dial",
    "addiesdive-ad2105-puck-diver": "Addiesdive AD2105 puck diver watch automatic 200m"
}

headers = {
    "Accept": "application/json",
    "X-Subscription-Token": API_KEY
}

download_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_and_save(watch_id, query):
    out_path = os.path.join(IMG_DIR, f"{watch_id}.jpg")
    if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
        print(f"[{watch_id}] Already exists ({os.path.getsize(out_path)} bytes), skipping.")
        return True

    print(f"[{watch_id}] Searching for: {query}...")
    try:
        resp = requests.get(
            "https://api.search.brave.com/res/v1/images/search",
            headers=headers,
            params={"q": query, "count": 10, "safesearch": "strict"},
            timeout=10
        )
        if resp.status_code != 200:
            print(f"  Brave API error ({resp.status_code}): {resp.text[:100]}")
            return False

        data = resp.json()
        results = data.get("results", [])
        if not results:
            print("  No image results found.")
            return False

        for res in results:
            img_url = res.get("properties", {}).get("url")
            if not img_url:
                continue
            try:
                img_resp = requests.get(img_url, headers=download_headers, timeout=8)
                if img_resp.status_code == 200 and len(img_resp.content) > 5000:
                    img = Image.open(io.BytesIO(img_resp.content))
                    img = img.convert("RGB")
                    # Resize so maximum dimension is 800px, maintain aspect ratio
                    img.thumbnail((800, 800), Image.Resampling.LANCZOS)
                    img.save(out_path, "JPEG", quality=88, optimize=True)
                    print(f"  Saved {watch_id}.jpg ({img.size[0]}x{img.size[1]}, {os.path.getsize(out_path)} bytes)")
                    return True
            except Exception as e:
                continue

        print(f"  Failed to download any valid image for {watch_id}")
        return False
    except Exception as e:
        print(f"  Error searching for {watch_id}: {e}")
        return False

def main():
    success = 0
    total = len(SEARCH_QUERIES)
    for watch_id, query in SEARCH_QUERIES.items():
        if fetch_and_save(watch_id, query):
            success += 1
        time.sleep(0.4)
    print(f"\nDone: {success}/{total} images saved to {IMG_DIR}")

if __name__ == "__main__":
    main()
