import requests 
import os
from datetime import datetime, timedelta
from config import OMDB_API_KEY, RAWG_API_KEY
from concurrent.futures import ThreadPoolExecutor
import requests

import requests

def get_game_info(game_name):
    api_key = RAWG_API_KEY

    # 1) Search for game
    search_url = "https://api.rawg.io/api/games"
    params = {"key": api_key, "search": game_name}

    try:
        res = requests.get(search_url, params=params, timeout=10)
        res.raise_for_status()
        results = res.json().get("results", [])
    except:
        return None

    if not results:
        return None

    game = results[0]
    slug = game["slug"]

    # 2) Base details
    base_url = f"https://api.rawg.io/api/games/{slug}"
    base = requests.get(base_url, params={"key": api_key}).json()

    # 3) Screenshots
    shots_url = f"https://api.rawg.io/api/games/{slug}/screenshots"
    screenshots = requests.get(shots_url, params={"key": api_key}).json().get("results", [])

    # # 4) Movies (trailers)
    # movies_url = f"https://api.rawg.io/api/games/{slug}/movies"
    # movies = requests.get(movies_url, params={"key": api_key}).json().get("results", [])

    # # 5) DLC / Additions
    # additions_url = f"https://api.rawg.io/api/games/{slug}/additions"
    # additions = requests.get(additions_url, params={"key": api_key}).json().get("results", [])

    # # 6) Game series (franchise)
    # series_url = f"https://api.rawg.io/api/games/{slug}/game-series"
    # series = requests.get(series_url, params={"key": api_key}).json().get("results", [])

    # # 7) Achievements
    # ach_url = f"https://api.rawg.io/api/games/{slug}/achievements"
    # achievements = requests.get(ach_url, params={"key": api_key}).json().get("results", [])

    # FINAL MERGED RESULT
    full_info = {
        "Name": base.get("name"),
        # "Slug": slug,
        "Released": base.get("released"),
        # "Updated": base.get("updated"),
        "Playtime": base.get("playtime"),
        "Rating": base.get("rating"),
        "Metacritic": base.get("metacritic"),
        "ESRB": base.get("esrb_rating", {}).get("name"),

        "Genres": [g["name"] for g in base.get("genres", [])],
        "Tags": [t["name"] for t in base.get("tags", [])],
        "Platforms": [p["platform"]["name"] for p in base.get("platforms", [])],
        # "Parent Platforms": [p["platform"]["name"] for p in base.get("parent_platforms", [])],

        "Developers": [d["name"] for d in base.get("developers", [])],
        "Publishers": [p["name"] for p in base.get("publishers", [])],
        # "Stores": [
        #     {"store": s["store"]["name"], "url": s.get("url")}
        #     for s in base.get("stores", [])
        # ],

        "Description": base.get("description_raw"),
        # "Website": base.get("website"),
        # "Reddit": base.get("reddit_url"),

        # Media
        "Background Image": base.get("background_image"),
        # "Background Additional": base.get("background_image_additional"),

        # New endpoints:
        "Screenshots": [s.get("image") for s in screenshots],
        # "Trailers": [
        #     m.get("data", {}).get("max")
        #     for m in movies
        # ],

        # "DLC": [a.get("name") for a in additions],
        # "DLC Count": len(additions),

        # "Series": [s.get("name") for s in series],
        # "Series Count": len(series),

        # "Achievements Count": len(achievements),
        # "Achievements": [
            # {
            #     "name": a.get("name"),
            #     "description": a.get("description"),
            #     "image": a.get("image")
            # }
            # for a in achievements
        #],
    }


    for x,y in full_info.items():
        print(f"{x}: {y}")
    return full_info

