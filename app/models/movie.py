# app/models/movie.py
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Movie:
    id: Optional[int] = None             # DB auto-increment ID
    title: str = ""                      # Movie title
    year: Optional[int] = None           # Release year
    rating: Optional[float] = None       # IMDb or external rating
    user_rating: Optional[float] = None  # Personal rating
    runtime: Optional[int] = None        # Runtime in minutes
    poster_path: Optional[str] = None    # Online path to poster
    genres: Optional[List[str]] = None   # List of genres
    plot: Optional[str] = None           # Movie description / plot
    imdb_id: Optional[str] = None        # IMDb ID
    tmdb_id: Optional[int] = None        # TMDB ID
    last_update: Optional[str] = None    # Timestamp of last update (string or ISO format)
    section: str = "want to watch"       # # default section
    trailer: Optional[str] = None        # Trailer URL