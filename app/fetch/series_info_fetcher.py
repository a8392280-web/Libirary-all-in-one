import requests 
from config import OMDB_API_KEY, TMDB_API_KEY

def get_series_info(title_name):
    """
    Complete TV series info fetcher (TMDB + OMDb) with fallback:
    TMDB first, OMDb second if TMDB data missing.
    """

    print(f"📺 Searching for TV Series: '{title_name}'")

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
        # 1. SEARCH SERIES ON TMDB
        search_response = session.get(
            f"{TMDB_BASE}/search/tv",
            params={"query": title_name, "api_key": TMDB_API_KEY},
            timeout=10
        )

        if search_response.status_code != 200:
            print("❌ TMDB search error")
            return "no"

        results = search_response.json().get("results", [])
        if not results:
            print("❌ No TV show found")
            return "no"

        show = results[0]
        show_id = show["id"]
        show_name = show.get("name", "Unknown")
        print(f"✅ Found series: {show_name} (ID: {show_id})")

        # 2. GET DETAILS FROM TMDB
        details_response = session.get(
            f"{TMDB_BASE}/tv/{show_id}",
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

        # 3. TRAILER
        trailer = None
        for video in details.get("videos", {}).get("results", []):
            if video.get("type") == "Trailer" and video.get("site") == "YouTube":
                trailer = f"https://www.youtube.com/watch?v={video['key']}"
                break

        # 4. CREATOR
        creator = None
        created_by = details.get("created_by") or []
        if created_by:
            c = created_by[0]
            creator = f"{c['name']}, https://image.tmdb.org/t/p/w500{c['profile_path']}" if c.get("profile_path") else c.get("name")

        # 5. CAST
        cast = []
        for actor in details.get("credits", {}).get("cast", [])[:10]:
            cast.append({
                "name": actor.get("name"),
                "character": actor.get("character", ""),
                "profile": f"https://image.tmdb.org/t/p/w500{actor['profile_path']}" if actor.get("profile_path") else None
            })

        # 6. IMDb & OMDb fallback
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

        # 7. RECOMMENDATIONS
        recommendations = []
        for rec in details.get("recommendations", {}).get("results", [])[:12]:
            recommendations.append({
                "title": rec.get("name"),
                "poster": f"https://image.tmdb.org/t/p/w500{rec['poster_path']}" if rec.get("poster_path") else None,
                "year": rec.get("first_air_date", "")[:4] if rec.get("first_air_date") else "TBA",
                "id": rec.get("id"),
                "rating": rec.get("vote_average")
            })

        # 8. RUNTIME
        runtime_list = details.get("episode_run_time") or []
        runtime = runtime_list[0] if runtime_list else None

        # fallback from OMDb
        if not runtime and omdb_data.get("Runtime") and "min" in omdb_data.get("Runtime"):
            try:
                runtime = int(omdb_data["Runtime"].split()[0])
            except ValueError:
                runtime = None

        runtime = runtime if runtime else "Unknown"

        # 9. GENRES
        genres = [g["name"] for g in details.get("genres", [])]
        if not genres and omdb_data.get("Genre"):
            genres = [g.strip() for g in omdb_data.get("Genre").split(",")]

        # 10. YEAR
        first_air = details.get("first_air_date", "")
        year = first_air[:4] if first_air else (omdb_data.get("Year") or "Unknown")

        # 11. PLOT
        plot = details.get("overview") or omdb_data.get("Plot") or "No plot available"

        # 12. IMAGE
        image = details.get("poster_path")
        if image:
            image = f"https://image.tmdb.org/t/p/w500{image}"
        elif omdb_data.get("Poster") and omdb_data.get("Poster") != "N/A":
            image = omdb_data["Poster"]
        else:
            image = None
        
        # 13. SEASONS + EPISODE COUNT + TMDB season ID + season name
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

            # Count only normal seasons (not Season 0)
            if season_number and season_number != 0:
                total_seasons += 1

                if episode_count and isinstance(episode_count, int):
                    total_episodes += episode_count




        # 14. BUILD RESULT
        result = {
            "source": "Series",
            "name": details.get("name"),
            "year": year,
            "runtime": runtime,
            "seasons":seasons_list,
            "total_seasons": total_seasons,
            "total_episodes": total_episodes,
            "tmdb_rating": round(details.get("vote_average", 0), 1),
            "tmdb_votes": details.get("vote_count"),
            "imdb_rating": imdb_rating,
            "imdb_votes": imdb_votes,
            "metascore": metascore,
            "rotten_tomatoes": rotten_tomatoes,
            "tmdb_id": show_id,
            "imdb_id": imdb_id,
            "image": image,
            "plot": plot,
            "trailer": trailer,
            "genres": genres,
            "creator": creator,
            "cast": cast,
            # "recommendations": recommendations,  # optional
        }

        print("✅ Successfully built complete TV series data with OMDb fallback!")


        return result

    except Exception as e:
        print(f"❌ Error: {e}")
        return "no"

