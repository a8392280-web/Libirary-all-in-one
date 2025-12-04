# app/models/series.py
from dataclasses import dataclass
from typing import List, Optional, Dict, Any

@dataclass
class Series:
    id: Optional[int] = None                  # DB auto-increment ID
    title: str = ""                             # Series title
    year: Optional[int] = None                 # First air year
    runtime: Optional[int] = None              # Average episode runtime in minutes
    total_seasons: Optional[int] = None       # Total seasons
    total_episodes: Optional[int] = None      # Total episodes
    seasons: Optional[List[Dict[str, Any]]] = None  # Detailed seasons info
    genres: Optional[List[str]] = None         # List of genres
    plot: Optional[str] = None                 # Plot / description
    creator: Optional[str] = None              # Creator (first one)
    cast: Optional[List[Dict[str, Any]]] = None # Cast list
    tmdb_id: Optional[int] = None              # TMDb series ID
    imdb_id: Optional[str] = None              # IMDb ID
    tmdb_rating: Optional[float] = None        # TMDb vote average
    tmdb_votes: Optional[int] = None           # TMDb vote count
    imdb_rating: Optional[float] = None        # IMDb rating
    imdb_votes: Optional[int] = None           # IMDb votes
    user_rating: Optional[float] = None        # user rating
    metascore: Optional[int] = None            # Metascore (from OMDb)
    rotten_tomatoes: Optional[str] = None      # Rotten Tomatoes rating
    trailer: Optional[str] = None              # Trailer URL
    poster_path: Optional[str] = None           # Poster URL
    last_update: Optional[str] = None          # Timestamp of last update
    section: str = "want to watch"             # Default section
