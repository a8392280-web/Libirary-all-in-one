# app/models/series.py

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class Series:
    id: Optional[int] = None                      # DB auto-increment ID
    title: str = ""                               # Series title
    year: Optional[int] = None                    # First air year
    runtime: Optional[int] = None                 # Avg episode runtime (minutes)
    poster_path: Optional[str] = None             # Poster URL
    genres: Optional[List[str]] = field(default_factory=list)   # List of genres
    plot: Optional[str] = None                    # Series description / plot
    imdb_id: Optional[str] = None                 # IMDb ID
    tmdb_id: Optional[int] = None                 # TMDB ID
    mal_id: Optional[int] = None                  # mal ID
    total_seasons: Optional[int] = None           # Total seasons count
    total_episodes: Optional[int] = None          # Total episodes count
    seasons: Optional[List[Dict[str, Any]]] = field(default_factory=list)  # Detailed seasons info
    cast: Optional[List[Dict[str, Any]]] = field(default_factory=list)     # Cast list
    creator: Optional[str] = None                 # Main creator
    trailer: Optional[str] = None                 # Trailer URL
    user_rating: Optional[float] = None           # Personal rating
    imdb_rating: Optional[float] = None           # IMDb rating
    imdb_votes: Optional[int] = None              # IMDb votes
    tmdb_rating: Optional[float] = None           # TMDB rating
    tmdb_votes: Optional[int] = None              # TMDB votes
    mal_rating: Optional[float] = None            # mal rating
    rotten_tomatoes: Optional[str] = None         # Rotten Tomatoes rating
    metascore: Optional[int] = None               # Metascore
    last_update: Optional[str] = None             # Last update timestamp
    section: str = "want to watch"                # Default section


SERIES_COLUMNS = [
    "title", "year", "runtime", "plot", "poster_path",
    "genres", "total_seasons", "total_episodes", "seasons",
    "imdb_rating", "user_rating", "tmdb_rating", "tmdb_votes",
    "imdb_votes", "rotten_tomatoes", "metascore",
    "imdb_id", "tmdb_id", "creator", "cast",
    "trailer", "section", "last_update",
    "mal_id", "mal_rating",
]
