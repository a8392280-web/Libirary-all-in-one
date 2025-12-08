import requests 
import os
from datetime import datetime, timedelta
from config import OMDB_API_KEY, TMDB_API_KEY, MY_ANIME_LIST
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from urllib.parse import quote
from difflib import get_close_matches
import time
import json
import re



TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w200"

def search_movies_tmdb(query, max_results=10):
    params = {"api_key": TMDB_API_KEY, "query": query, "include_adult": False, "page": 1}
    response = requests.get(TMDB_SEARCH_URL, params=params)
    if response.status_code != 200:
        return []
    data = response.json()
    results = []
    for movie in data.get("results", [])[:max_results]:
        poster_path = movie.get("poster_path")
        poster_url = f"{TMDB_IMAGE_BASE}{poster_path}" if poster_path else None
        results.append({
            "title": movie.get("title"),
            "id": movie.get("id"),
            "poster_url": poster_url,
            "overview": movie.get("overview"),
            "release_date": movie.get("release_date"),
        })
    return results



def get_movie_info(movie_id):
    """
    Complete movie info fetcher using TMDB ID + OMDb for IMDb data.
    """
    if not TMDB_API_KEY:
        print("❌ TMDB_API_KEY is missing!")
        return "no"
    if not OMDB_API_KEY:
        print("❌ OMDB_API_KEY is missing!")
        return "no"

    TMDB_BASE = "https://api.themoviedb.org/3"
    OMDB_BASE = "https://www.omdbapi.com/"
    session = requests.Session()

    try:
        # 1. GET MOVIE DETAILS
        details_response = session.get(
            f"{TMDB_BASE}/movie/{movie_id}",
            params={
                "api_key": TMDB_API_KEY,
                "append_to_response": "videos,credits,recommendations"
            },
            timeout=10
        )
        if details_response.status_code != 200:
            print(f"❌ TMDB Details failed with status: {details_response.status_code}")
            return "no"
        details = details_response.json()
        movie_title = details.get("title", "Unknown")
        print(f"✅ Found movie: {movie_title} (ID: {movie_id})")

        # 2. GET TRAILER
        trailer = None
        for video in details.get("videos", {}).get("results", []):
            if video.get("type") == "Trailer" and video.get("site") == "YouTube":
                trailer = f"https://www.youtube.com/watch?v={video['key']}"
                break

        # 3. GET DIRECTOR + WRITERS + CAST
        director = None
        writers = []
        cast = []

        for crew in details.get("credits", {}).get("crew", []):
            if crew.get("job") == "Director":
                director = f"{crew['name']}, https://image.tmdb.org/t/p/w500{crew.get('profile_path')}"
            if crew.get("job") in ["Writer", "Screenplay", "Author"]:
                if crew['name'] not in writers:
                    writers.append(crew['name'])

        for actor in details.get("credits", {}).get("cast", [])[:10]:
            cast.append({
                "name": actor["name"],
                "character": actor.get("character", ""),
                "profile": f"https://image.tmdb.org/t/p/w500{actor['profile_path']}" if actor.get("profile_path") else None,
                "order": actor.get("order", 999)
            })

        # 4. GET IMDb info via OMDb
        imdb_rating = None
        imdb_votes = None
        metascore = None
        rotten_tomatoes = None
        box_office = None
        awards = None
        imdb_id = details.get("imdb_id")

        if imdb_id and OMDB_API_KEY:
            try:
                omdb_response = session.get(
                    OMDB_BASE,
                    params={
                        "apikey": OMDB_API_KEY,
                        "i": imdb_id,
                        "plot": "full"
                    },
                    timeout=10
                )
                if omdb_response.status_code == 200:
                    omdb_data = omdb_response.json()
                    if omdb_data.get("Response") == "True":
                        imdb_rating = omdb_data.get("imdbRating")
                        imdb_votes = omdb_data.get("imdbVotes")
                        metascore = omdb_data.get("Metascore",None)
                        box_office = omdb_data.get("BoxOffice")
                        awards = omdb_data.get("Awards")
                        for rating in omdb_data.get("Ratings", []):
                            if rating["Source"] == "Rotten Tomatoes":
                                rotten_tomatoes = rating["Value"]
                                break
            except Exception as e:
                print(f"❌ OMDb error: {e}")

        # 5. BUILD RESULT
        release_date = details.get("release_date", "")
        year = release_date[:4] if release_date else "Unknown"
        result = {
            "source": "Movie",
            "name": movie_title,
            "year": year,
            "runtime": details.get("runtime"),
            "tmdb_rating": round(details.get("vote_average", 0), 1),
            "tmdb_votes": details.get("vote_count"),
            "imdb_rating": imdb_rating,
            "imdb_votes": imdb_votes,
            "rotten_tomatoes": rotten_tomatoes,
            "metascore": metascore,
            "tmdb_id": movie_id,
            "imdb_id": imdb_id,
            "image": f"https://image.tmdb.org/t/p/w500{details.get('poster_path')}" if details.get("poster_path") else None,
            "plot": details.get("overview"),
            "trailer": trailer,
            "genres": [g["name"] for g in details.get("genres", [])],
            "director": director,
            "cast": cast,
        }

        print("✅ Successfully built complete movie data!")
        return result

    except requests.exceptions.Timeout:
        print("❌ Request timed out")
        return "no"
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - check internet")
        return "no"
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return "no"






MAL_SEARCH_URL = "https://api.myanimelist.net/v2/anime"

def search_anime_movies(query, max_results=20):
    headers = {"X-MAL-CLIENT-ID": MY_ANIME_LIST}
    params = {
        "q": query,
        "limit": max_results,
        "fields": "id,title,main_picture,media_type,start_date,synopsis"
    }
    
    response = requests.get(MAL_SEARCH_URL, headers=headers, params=params)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return []
    
    data = response.json()
    results = []
    
    movie_types = ["movie", "ova", "special", "ona"]
    
    for anime in data.get("data", []):
        node = anime.get("node", {})
        media_type = node.get("media_type")

        if media_type not in movie_types:
            continue
        
        main_picture = node.get("main_picture", {})
        poster_url = main_picture.get("medium")
        
        results.append({
            "title": node.get("title"),
            "id": node.get("id"),
            "poster_url": poster_url,
            "synopsis": node.get("synopsis"),
            "start_date": node.get("start_date"),
            "type": media_type,
        })
    
    return results



import requests


MAL_BASE_URL = "https://api.myanimelist.net/v2/anime"

def get_movies_anime_info(anime_id):
    """
    Complete anime info fetcher using MyAnimeList anime ID.
    """
    headers = {"X-MAL-CLIENT-ID": MY_ANIME_LIST}
    params = {
        "fields": "id,title,main_picture,media_type,num_episodes,start_date,genres,studios,synopsis,alternative_titles,end_date,mean"
    }

    try:
        response = requests.get(f"{MAL_BASE_URL}/{anime_id}", headers=headers, params=params, timeout=10)
        if response.status_code != 200:
            print(f"❌ MAL API returned status {response.status_code}")
            return "no"

        data = response.json()

        # Basic info
        anime_title = data.get("title")
        start_date = data.get("start_date")
        end_date = data.get("end_date")
        year = start_date[:4] if start_date else "Unknown"
        synopsis = data.get("synopsis")
        episodes = data.get("num_episodes")
        media_type = data.get("media_type")
        rating = data.get("mean")  # average user score

        # Images
        main_picture = data.get("main_picture", {})
        poster_url = main_picture.get("medium")
        large_poster_url = main_picture.get("large")
        background = data.get("background")
        extra_pictures = [pic.get("large") for pic in data.get("pictures", [])]

        # Genres and studios
        genres = [g["name"] for g in data.get("genres", [])]
        studios = [s["name"] for s in data.get("studios", [])]

        # Alternative titles
        alt_titles = data.get("alternative_titles", {})

        # Build result dict
        result = {
            "source": "movie",
            "name": anime_title,
            "year": year,
            # "start_date": start_date,
            # "end_date": end_date,
            # "episodes": episodes,
            # "type": media_type,
            "mal_rating": rating,
            "mal_id": anime_id,
            "image": poster_url,
            # "poster_large": large_poster_url,
            # "background": background,
            # "extra_pictures": extra_pictures,
            "plot": synopsis,
            "genres": genres,
            # "studios": studios,
            # "alternative_titles": alt_titles
        }
        print(result)
        print(f"✅ Successfully fetched anime: {anime_title} (ID: {anime_id})")
        return result

    except requests.exceptions.Timeout:
        print("❌ Request timed out")
        return "no"
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - check internet")
        return "no"
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return "no"



















































def get_best_match(movie_name, movies_list, cutoff=0.5):
    if not movies_list:
        return None

    titles = [m["name"] for m in movies_list]
    best_title = get_close_matches(movie_name, titles, n=1, cutoff=cutoff)

    if best_title:
        for m in movies_list:
            if m["name"] == best_title[0]:
                return m["link"]
    return None


class ArabSeedScraper:
    """Get movie name and return watch page link in arabseed site"""
    def __init__(self, name, user_agent="Mozilla/5.0"):
        self.headers = {"User-Agent": user_agent}
        self.base_url = "https://a.asd.homes"
        self.watch_url = self.search_best_movie(name)
        print(self.watch_url)

    def scrape_movies(self, movie_name):
        encoded_name = quote(movie_name)
        url = f"{self.base_url}/find/?word={encoded_name}&type="

        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        containers = soup.select("div.series__list ul")

        movies_info = []
        for ul in containers:
            for tag in ul.select("a.movie__block"):
                title = tag.get("title")
                link = tag.get("href")
                if title and link:
                    # Ensure full absolute URL
                    full_url = link if link.startswith("http") else self.base_url + link
                    movies_info.append({"name": title, "link": full_url})

        return movies_info


    def get_watch_page(self, link):
        time.sleep(0.3)

        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")

        watch_button = soup.select_one("a.watch__btn")

        if not watch_button:
            print("❌ Watch button not found!")
            return None

        watch_page_link = watch_button.get("href")

        full_watch_link = (
            watch_page_link if watch_page_link.startswith("http")
            else self.base_url + watch_page_link
        )

        return full_watch_link

    def search_best_movie(self, movie_name, cutoff=0.5):
        movies_list = self.scrape_movies(movie_name)
        best_match_link = get_best_match(movie_name, movies_list, cutoff)

        if not best_match_link:
            print("❌ No match found.")
            return None

        return self.get_watch_page(best_match_link)


class AkwamScraper:
    def __init__(self, name, year=0, user_agent="Mozilla/5.0"):
        self.headers = {"User-Agent": user_agent}
        self.base_url = "https://ak.sv"
        self.year = int(year)
        self.watch_url = self.search_best_movie(name)
        print(self.watch_url)
        

    def scrape_movies(self, movie_name):
        encoded_name = quote(movie_name)
        url = f"{self.base_url}/search?q={encoded_name}&section=movie&year={self.year}&rating=0&formats=0&quality=0"

        response = requests.get(url, headers=self.headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # REAL MOVIE CARDS
        containers = soup.select("div.col-lg-auto.col-md-4.col-6.mb-12")
 
        if not containers:
            print("No results found! (Selector wrong or blocked)")
            return []

        movies_info = []

        for div in containers:
            tag = div.select_one("h3.entry-title a")
            if not tag:
                continue

            title = tag.text.strip()
            link = tag.get("href", "")

            if link.startswith("/"):
                link = self.base_url + link


            movies_info.append({"name": title, "link": link})

        return movies_info


    def search_best_movie(self, movie_name, cutoff=0.5):
        movies_list = self.scrape_movies(movie_name)
        best_match_link = get_best_match(movie_name, movies_list, cutoff)

        if not best_match_link:
            print("❌ No match found.")
            return None

        return best_match_link




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


