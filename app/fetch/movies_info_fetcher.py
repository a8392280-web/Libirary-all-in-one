import requests 
import os
from datetime import datetime, timedelta
from config import OMDB_API_KEY, TMDB_API_KEY
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from urllib.parse import quote
from difflib import get_close_matches
import time
import json
import re


def get_movie_info(title_name):
    """
    Complete movie info fetcher with all details from TMDB + IMDb
    """
    print(f"🎬 Searching for: '{title_name}'")
    
    # Check API keys
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
        # 1. SEARCH MOVIE
        # print("🔍 Step 1: Searching TMDB...")
        search_response = session.get(
            f"{TMDB_BASE}/search/movie",
            params={
                "query": title_name, 
                "api_key": TMDB_API_KEY
            },
            timeout=10
        )
        
        if search_response.status_code != 200:
            print(f"❌ TMDB Search failed with status: {search_response.status_code}")
            return "no"
            
        search_data = search_response.json()
        # print(f"📊 Found {len(search_data.get('results', []))} results")
        
        if not search_data.get("results"):
            print("❌ No movies found with that title")
            return "no"
        
        # Get first movie result
        movie = search_data["results"][0]
        movie_id = movie["id"]
        movie_title = movie.get("title", "Unknown")
        print(f"✅ Found movie: {movie_title} (ID: {movie_id})")
        
        # 2. GET MOVIE DETAILS
        print("🔍 Step 2: Fetching movie details...")
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
        # print(f"✅ Got details for: {details.get('title')}")
        
        # 3. GET TRAILER
        trailer = None
        videos = details.get("videos", {}).get("results", [])
        # print(f"🎥 Found {len(videos)} videos")
        
        for video in videos:
            if video.get("type") == "Trailer" and video.get("site") == "YouTube":
                trailer = f"https://www.youtube.com/watch?v={video['key']}"
                # print(f"✅ Found trailer: {trailer}")
                break
        
        # 4. GET DIRECTOR + WRITERS
        director = None
        writers = []
        producers = []
        composers = []
        
        for crew in details.get("credits", {}).get("crew", []):
            if crew.get("job") == "Director":
                director = f"{crew["name"]}, https://image.tmdb.org/t/p/w500{crew["profile_path"]}"
            if crew.get("job") in ["Writer", "Screenplay", "Author"]:
                if crew["name"] not in writers:  # Avoid duplicates
                    writers.append(crew["name"])
            if crew.get("job") == "Producer":
                producers.append(crew["name"])
            if crew.get("job") == "Original Music Composer":
                composers.append(crew["name"])
        
        # print(f"🎬 Director: {director}")
        # print(f"✍️ Writers: {writers[:3]}")  # Show first 3
        
        # 5. GET CAST (TOP 15)
        cast = []
        for actor in details.get("credits", {}).get("cast", [])[:10]:
            cast.append({
                "name": actor["name"],
                "character": actor.get("character", ""),
                "profile": f"https://image.tmdb.org/t/p/w500{actor['profile_path']}" if actor.get("profile_path") else None,
                "order": actor.get("order", 999)
            })
        
        # print(f"🌟 Cast: {len(cast)} actors")
        
        # 6. GET IMDb RATING & ADDITIONAL DATA
        imdb_rating = None
        rotten_tomatoes = None
        metascore = None
        imdb_votes = None
        box_office = None
        awards = None
        rated = None
        dvd_release = None
        website = None
        
        imdb_id = details.get("imdb_id")
        # print(f"📊 IMDb ID: {imdb_id}")
        
        if imdb_id and OMDB_API_KEY:
            try:
                # print("🔍 Step 3: Fetching IMDb rating from OMDb...")
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
                        metascore = omdb_data.get("Metascore")
                        box_office = omdb_data.get("BoxOffice")
                        awards = omdb_data.get("Awards")
                        rated = omdb_data.get("Rated")
                        dvd_release = omdb_data.get("DVD")
                        website = omdb_data.get("Website")
                        
                        # Get Rotten Tomatoes rating
                        for rating in omdb_data.get("Ratings", []):
                            if rating["Source"] == "Rotten Tomatoes":
                                rotten_tomatoes = rating["Value"]
                                break
                        
                        # print(f"⭐ IMDb Rating: {imdb_rating}")
                        # print(f"🍅 Rotten Tomatoes: {rotten_tomatoes}")
                        # print(f"📈 Metascore: {metascore}")
                    else:
                        print("❌ OMDb response was False")
                else:
                    print(f"❌ OMDb request failed: {omdb_response.status_code}")
                    
            except Exception as e:
                print(f"❌ OMDb error: {e}")
        
        # 7. RECOMMENDATIONS (TOP 12)
        recommendations = []
        for rec in details.get("recommendations", {}).get("results", [])[:12]:
            recommendations.append({
                "title": rec["title"],
                "poster": f"https://image.tmdb.org/t/p/w500{rec['poster_path']}" if rec.get("poster_path") else None,
                "year": rec.get('release_date', '')[:4] if rec.get('release_date') else 'TBA',
                "id": rec["id"],
                "rating": rec.get("vote_average")
            })
        
        # print(f"🔗 Recommendations: {len(recommendations)} movies")
        
        # 8. BUILD COMPLETE RESPONSE
        # print("📦 Building complete response...")
        
        # Get year from release date
        release_date = details.get("release_date", "")
        year = release_date[:4] if release_date else "Unknown"
        
        # Format budget and revenue
        budget = details.get("budget")
        revenue = details.get("revenue")
        
        def format_currency(amount):
            if not amount or amount == 0:
                return None
            return f"${amount:,}"
        
        # Get all languages and countries
        languages = [lang["english_name"] for lang in details.get("spoken_languages", [])]
        countries = [country["name"] for country in details.get("production_countries", [])]
        companies = [company["name"] for company in details.get("production_companies", [])]
        result = {
            "source": "Movie",
            
            # BASIC DATA
            "name": details.get("title"),
            # "OriginalName": details.get("original_title"),
            # "Tagline": details.get("tagline"),
            "year": year,
            # "ReleaseDate": details.get("release_date"),
            # "Status": details.get("status"),
            "runtime": details.get("runtime"),
            
            # RATINGS
            "tmdb_rating": round(details.get("vote_average", 0), 1),
            "tmdb_votes": details.get("vote_count"),
            "imdb_rating": imdb_rating,
            "imdb_votes": imdb_votes,
            "rotten_tomatoes": rotten_tomatoes,
            "metascore": metascore,
            # "rated": rated,
            
            # IDs
            "tmdb_id": movie_id,
            "imdb_id": imdb_id,
            
            # POSTERS & IMAGES
            "image": f"https://image.tmdb.org/t/p/w500{details.get('poster_path')}" if details.get("poster_path") else None,
            #"Backdrop": f"https://image.tmdb.org/t/p/original{details.get('backdrop_path')}" if details.get("backdrop_path") else None,
            
            # PLOT
            "plot": details.get("overview"),
            
            # TRAILER
            "trailer": trailer,
            
            # GENRES
            "genres": [g["name"] for g in details.get("genres", [])],
            
            # # LANGUAGE / COUNTRY / PRODUCTION
            # "Languages": languages,
            # "Countries": countries,
            # "Companies": companies,
            
            # # HOMEPAGE
            # "Homepage": details.get("homepage"),
            # "Website": website,
            
            # # BUDGET & REVENUE
            # "Budget": format_currency(budget),
            # "Revenue": format_currency(revenue),
            # "BoxOffice": box_office,
            
            # # CAST & CREW
            "director": director,
            # "Writers": writers,
            # "Producers": producers[:5],  # Top 5 producers
            # "Composers": composers,
            "cast": cast,
            
            # # RECOMMENDATIONS
            # "Recommendations": recommendations,
            
            # # AWARDS & RELEASES
            # "Awards": awards,
            # "DVD": dvd_release,
            
            # # ADDITIONAL INFO
            # "Popularity": round(details.get("popularity", 0), 1),
            # "Adult": details.get("adult", False),
            # "Video": details.get("video", False)
        }
        
        print("✅ Successfully built complete movie data!")
        print("🎬 Movie:", result["tmdb_id"])
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


