# app/models/movie.py

from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class Movie:
    id: Optional[int] = None             # DB auto-increment ID
    title: str = ""                      # Movie title
    year: Optional[int] = None           # Release year
    imdb_rating: Optional[float] = None  # IMDb or external rating
    user_rating: Optional[float] = None  # Personal rating
    runtime: Optional[int] = None        # Runtime in minutes
    poster_path: Optional[str] = None    # Online path to poster
    genres: Optional[List[str]] = field(default_factory=list)   # List of genres
    plot: Optional[str] = None           # Movie description / plot
    imdb_id: Optional[str] = None        # IMDb ID
    tmdb_id: Optional[int] = None        # TMDB ID
    last_update: Optional[str] = None    # Timestamp of last update (string or ISO format)
    section: str = "want to watch"       # Default section
    trailer: Optional[str] = None        # Trailer URL
    cast: Optional[List[Dict]] = field(default_factory=list)    # Movie cast
    director: Optional[str] = None       # Director
    tmdb_rating: Optional[float] = None  # TMDB rating
    tmdb_votes: Optional[int] = None     # TMDB votes
    imdb_votes: Optional[int] = None     # IMDb votes
    rotten_tomatoes: Optional[str] = None # Rotten Tomatoes rating
    metascore: Optional[int] = None      # Metascore
    mal_rating: Optional[float] = None     # MyAnimeList rating / new column
    mal_id: Optional[int] = None


# Column list for dynamic CRUD operations
MOVIE_COLUMNS = [
    "title", "year", "runtime", "plot", "poster_path",
    "genres", "imdb_rating", "user_rating", "tmdb_rating", "tmdb_votes",
    "imdb_votes", "rotten_tomatoes", "metascore",
    "imdb_id", "tmdb_id", "director", "cast",
    "trailer", "section", "last_update",
    "mal_rating", "mal_id"  # New column
]
