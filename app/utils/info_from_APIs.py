import requests 
import os
from datetime import datetime, timedelta
from config import OMDB_API_KEY, RAWG_API_KEY


def get_movie_info(title_name):
    "fetch data by name from omdb"
    url = "http://www.omdbapi.com/"
    params = {
        "t": title_name,
        "apikey": OMDB_API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"❌ OMDB API error: {e}")
        return None

    if data.get("Response") != "True":
        print("❌ Title not found.")
        return "no"

    # Detect type
    media_type = data.get("Type", "").capitalize()  # 'Movie' or 'Series'
    movie_info = {
        "Source": media_type,
        "Name": data.get("Title") or "Unknown",
        "Released": data.get("Year") or "Unknown",
        "Rating": data.get("imdbRating") or "N/A",
        "imdb_id": data.get("imdbID")  or "N/A",
        "Genres": [genre.strip() for genre in data.get("Genre", "").split(",")] if data.get("Genre") else [],
        "Image": data.get("Poster") or "N/A",
        "Plot": data.get("Plot") or "N/A",
        "Runtime": data.get("Runtime") or "Unknown"
    }
    
    return movie_info


def update_imdb_info_if_old(movie):
    """Update IMDb rating if data is older than 7 days."""
    API_KEY = "OMDB_API_KEY"
    updated = movie.copy()  # ✅ Make a separate copy
    try:
        last_updated = datetime.fromisoformat(movie.get("last_updated", "1970-01-01"))
    except ValueError:
        last_updated = datetime(1970, 1, 1)

    # Check if older than 7 days
    if datetime.now() - last_updated > timedelta(days=7):
        imdb_id = movie.get("imdb_id")
        if not imdb_id:
            return None  # No IMDb ID, can’t update

        url = f"https://www.omdbapi.com/?i={imdb_id}&apikey={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("Response") == "True":
                updated["Rating"] = data.get("imdbRating", movie.get("Rating", "N/A"))
                updated["last_updated"] = datetime.now().isoformat()
                print(f"✅ Updated IMDb rating for {movie.get('Name')}: {movie['Rating']}")
                return updated
        else:
            print(f"⚠️ Failed to update IMDb data for {movie.get('Name')}")

            return None

    return None


def get_game_info(game_name):
    api_key = RAWG_API_KEY
    url = "https://api.rawg.io/api/games"
    params = {
        "key": api_key,
        "search": game_name
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"❌ RAWG API error: {e}")
        return None

    if not data.get("results"):
        print("❌ No game found.")
        return None

    game = data["results"][0]
    game_info = {
        "Source": "Game",
        "Name": game.get("name") or "Unknown",
        "Released": game.get("released") or "Unknown",
        "Rating": game.get("rating") or "N/A",
        "Genres": [genre.get("name", "Unknown") for genre in game.get("genres", [])],
        "Image": game.get("background_image") or "N/A",
        "Platforms": [platform.get("platform", {}).get("name", "Unknown") for platform in game.get("platforms", [])]
    }

    # Loop until user approves
    
    print("\n🎮 Game Information:\n")
    for key, value in game_info.items():
        print(f"{key}: {value}")

    choice = input("\nDo you want to change any field? (yes/no): ").strip().lower()
    if choice == "yes":
        while True:

            for key in game_info.keys():
                if key == "Source":  # Can't change Source
                    continue

                new_value = input(f"Enter new value for '{key}' (leave empty to keep current): ").strip()
                if new_value:
                    if key in ("Genres", "Platforms"):
                        game_info[key] = [item.strip() for item in new_value.split(",")]
                    else:
                        game_info[key] = new_value

            print("\n✅ Updated Game Information:")
            for key, value in game_info.items():
                print(f"{key}: {value}")

            confirm = input("\nAre these changes good? (yes/no): ").strip().lower()
            if confirm == "yes":
                break
        

    return game_info


def get_manga_info(manga_name):
    url = 'https://kitsu.io/api/edge/manga'
    params = {'filter[text]': manga_name}

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Kitsu API error: {e}")
        return None

    data = resp.json()
    manga_list = data.get('data', [])
    if not manga_list:
        print("❌ Manga not found.")
        return None

    manga = manga_list[0]
    manga_id = manga.get('id')
    attributes = manga.get('attributes', {})

    # Fetch genres
    try:
        genre_url = f"https://kitsu.io/api/edge/manga/{manga_id}/genres"
        genre_resp = requests.get(genre_url, timeout=10)
        genre_resp.raise_for_status()
        genres_data = genre_resp.json().get('data', [])
        genres = [g.get('attributes', {}).get('name', 'Unknown') for g in genres_data]
    except requests.RequestException:
        genres = ["Unknown"]

    manga_info = {
        "Source": "Manga",
        "Name": attributes.get('titles', {}).get('en_jp', 'Unknown'),
        "Released": attributes.get('startDate') or "Unknown",
        "Rating": "N/A",
        "Genres": genres,
        "Image": attributes.get('posterImage', {}).get('small', 'N/A'),
        "Plot": attributes.get('synopsis') or "N/A",
        "Chapters": attributes.get('chapterCount') or "Unknown"
    }


    print("\n📚 Manga Information:")
    for key, value in manga_info.items():
        print(f"{key}: {value}")

    choice = input("\nDo you want to change any field? (yes/no): ").strip().lower()
    if choice == "yes":
        while True:
            for key in manga_info.keys():
                if key == "Source":  # Cannot change source
                    continue

                new_value = input(f"Enter new value for '{key}' (leave empty to keep current): ").strip()
                if new_value:
                    if key == "Genres":
                        manga_info[key] = [genre.strip() for genre in new_value.split(",")]
                    else:
                        manga_info[key] = new_value

            print("\n✅ Updated Manga Information:")
            for key, value in manga_info.items():
                print(f"{key}: {value}")

            confirm = input("\nAre these changes good? (yes/no): ").strip().lower()
            if confirm == "yes":
                break

    return manga_info

