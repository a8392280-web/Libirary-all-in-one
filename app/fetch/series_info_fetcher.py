import requests 
from config import OMDB_API_KEY, TMDB_API_KEY, MY_ANIME_LIST


TMDB_SEARCH_TV = "https://api.themoviedb.org/3/search/tv"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w200"

def search_series_tmdb(query, max_results=10):
    """
    Search TMDB for TV series.

    :param query: Search string
    :param max_results: Maximum number of results to return
    :return: List of dicts with title, id, poster_url, overview, release_date
    """
    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "include_adult": False,
        "page": 1
    }

    response = requests.get(TMDB_SEARCH_TV, params=params)
    if response.status_code != 200:
        return []

    data = response.json()
    results = []
    for series in data.get("results", [])[:max_results]:
        poster_path = series.get("poster_path")
        poster_url = f"{TMDB_IMAGE_BASE}{poster_path}" if poster_path else None

        release_date = series.get("first_air_date") or "Unknown"

        results.append({
            "title": series.get("name"),
            "id": series.get("id"),
            "poster_url": poster_url,
            "overview": series.get("overview"),
            "release_date": release_date
        })

    return results



def get_series_info(tmdb_id):
    """
    Complete TV series info fetcher (TMDB + OMDb) with fallback:
    TMDB first, OMDb second if TMDB data missing.
    Accepts TMDB series ID directly.
    """

    print(f"📺 Fetching TV Series with TMDB ID: {tmdb_id}")

    if not TMDB_API_KEY:
        print("❌ TMDB_API_KEY missing!")
        return "no"
    if not OMDB_API_KEY:
        print("❌ OMDB_API_KEY missing!")
        return "no"

    TMDB_BASE = "https://api.themoviedb.org/3"
    OMDB_BASE = "https://www.omdbapi.com/"
    session = requests.Session()

    try:
        # 1. GET DETAILS FROM TMDB
        details_response = session.get(
            f"{TMDB_BASE}/tv/{tmdb_id}",
            params={
                "api_key": TMDB_API_KEY,
                "append_to_response": "videos,credits,recommendations,external_ids"
            },
            timeout=10
        )

        if details_response.status_code != 200:
            print("❌ Failed to get TV details")
            return "no"

        details = details_response.json()

        show_name = details.get("name", "Unknown")
        print(f"✅ Found series: {show_name} (ID: {tmdb_id})")

        # 2. TRAILER
        trailer = None
        for video in details.get("videos", {}).get("results", []):
            if video.get("type") == "Trailer" and video.get("site") == "YouTube":
                trailer = f"https://www.youtube.com/watch?v={video['key']}"
                break

        # 3. CREATOR
        creator = None
        created_by = details.get("created_by") or []
        if created_by:
            c = created_by[0]
            creator = f"{c['name']}, https://image.tmdb.org/t/p/w500{c['profile_path']}" if c.get("profile_path") else c.get("name")

        # 4. CAST
        cast = []
        for actor in details.get("credits", {}).get("cast", [])[:10]:
            cast.append({
                "name": actor.get("name"),
                "character": actor.get("character", ""),
                "profile": f"https://image.tmdb.org/t/p/w500{actor['profile_path']}" if actor.get("profile_path") else None
            })

        # 5. IMDb & OMDb fallback
        imdb_id = details.get("external_ids", {}).get("imdb_id")
        imdb_rating = imdb_votes = metascore = rotten_tomatoes = None
        omdb_data = {}

        if imdb_id:
            omdb = session.get(
                OMDB_BASE,
                params={"apikey": OMDB_API_KEY, "i": imdb_id, "plot": "full"},
                timeout=10
            )
            if omdb.status_code == 200:
                o = omdb.json()
                if o.get("Response") == "True":
                    omdb_data = o
                    imdb_rating = o.get("imdbRating")
                    imdb_votes = o.get("imdbVotes")
                    metascore = None if o.get("Metascore") in [None, "N/A"] else o.get("Metascore")
                    for r in o.get("Ratings", []):
                        if r.get("Source") == "Rotten Tomatoes":
                            rotten_tomatoes = r.get("Value")
                            break

        # 6. RECOMMENDATIONS
        recommendations = []
        for rec in details.get("recommendations", {}).get("results", [])[:12]:
            recommendations.append({
                "title": rec.get("name"),
                "poster": f"https://image.tmdb.org/t/p/w500{rec['poster_path']}" if rec.get("poster_path") else None,
                "year": rec.get("first_air_date", "")[:4] if rec.get("first_air_date") else "TBA",
                "id": rec.get("id"),
                "rating": rec.get("vote_average")
            })

        # 7. RUNTIME
        runtime_list = details.get("episode_run_time") or []
        runtime = runtime_list[0] if runtime_list else None

        if not runtime and omdb_data.get("Runtime") and "min" in omdb_data.get("Runtime"):
            try:
                runtime = int(omdb_data["Runtime"].split()[0])
            except ValueError:
                runtime = None
        runtime = runtime if runtime else "Unknown"

        # 8. GENRES
        genres = [g["name"] for g in details.get("genres", [])]
        if not genres and omdb_data.get("Genre"):
            genres = [g.strip() for g in omdb_data.get("Genre").split(",")]

        # 9. YEAR
        first_air = details.get("first_air_date", "")
        year = first_air[:4] if first_air else (omdb_data.get("Year") or "Unknown")

        # 10. PLOT
        plot = details.get("overview") or omdb_data.get("Plot") or "No plot available"

        # 11. IMAGE
        image = details.get("poster_path")
        if image:
            image = f"https://image.tmdb.org/t/p/w500{image}"
        elif omdb_data.get("Poster") and omdb_data.get("Poster") != "N/A":
            image = omdb_data["Poster"]
        else:
            image = None

        # 12. SEASONS + EPISODE COUNT + TMDB season ID + season name
        seasons_list = []
        total_seasons = 0
        total_episodes = 0

        for season in details.get("seasons", []):
            season_number = season.get("season_number")
            episode_count = season.get("episode_count")
            season_name = season.get("name") or f"Season {season_number}"
            season_tmdb_id = season.get("id")
            air_date = season.get("air_date") or "Unknown"

            if season_number is not None:
                seasons_list.append({
                    "season_number": season_number,
                    "season_name": season_name,
                    "tmdb_season_id": season_tmdb_id,
                    "episode_count": episode_count if episode_count is not None else "TBA",
                    "air_date": air_date
                })

            if season_number and season_number != 0:
                total_seasons += 1
                if episode_count and isinstance(episode_count, int):
                    total_episodes += episode_count

        # 13. BUILD RESULT
        result = {
            "source": "Series",
            "name": details.get("name"),
            "year": year,
            "runtime": runtime,
            "seasons": seasons_list,
            "total_seasons": total_seasons,
            "total_episodes": total_episodes,
            "tmdb_rating": round(details.get("vote_average", 0), 1),
            "tmdb_votes": details.get("vote_count"),
            "imdb_rating": imdb_rating,
            "imdb_votes": imdb_votes,
            "metascore": metascore,
            "rotten_tomatoes": rotten_tomatoes,
            "tmdb_id": tmdb_id,
            "imdb_id": imdb_id,
            "image": image,
            "plot": plot,
            "trailer": trailer,
            "genres": genres,
            "creator": creator,
            "cast": cast,
        }

        print("✅ Successfully built complete TV series data with OMDb fallback!")
        return result

    except Exception as e:
        print(f"❌ Error: {e}")
        return "no"








MAL_SEARCH_URL = "https://api.myanimelist.net/v2/anime"

def search_anime_series(query, max_results=20):
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
    

    for anime in data.get("data", []):
        node = anime.get("node", {})
        media_type = node.get("media_type")

        if media_type != "tv":  # filter TV series only
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




MAL_BASE_URL = "https://api.myanimelist.net/v2/anime"

def get_series_anime_info(anime_id):
    """
    Complete anime info fetcher using MyAnimeList anime ID.
    """
    headers = {"X-MAL-CLIENT-ID": MY_ANIME_LIST}
    params = {
        "fields": "id,title,main_picture,media_type,num_episodes,start_date,genres,studios,synopsis,alternative_titles,end_date,mean,average_episode_duration"
    }

    try:
        response = requests.get(f"{MAL_BASE_URL}/{anime_id}", headers=headers, params=params, timeout=10)
        if response.status_code != 200:
            print(f"❌ MAL API returned status {response.status_code}")
            return "no"

        data = response.json()

        # Basic info
        anime_title = data.get("title")
        runtime = runtime = data.get("average_episode_duration")
        if runtime is not None:
            runtime = runtime // 60  # integer minutes
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
            "source": "Anime",
            "name": anime_title,
            "year": year,
            "runtime": runtime,
            # "start_date": start_date,
            # "end_date": end_date,
            "total_episodes": episodes,
            "total_seasons" : 1,
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

