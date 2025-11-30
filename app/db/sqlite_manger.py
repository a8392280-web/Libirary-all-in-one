import sqlite3
from pathlib import Path
from app.models.movie import Movie
import json
from typing import Callable

# ==========================================================
# 📘 DATABASE SETUP
# ==========================================================
SCHEMA = """
-- ================================
-- MOVIES TABLE (FULL FEATURED)
-- ================================

CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- BASIC INFO
    title TEXT NOT NULL,
    year INTEGER,
    runtime INTEGER,
    plot TEXT,
    poster_path TEXT,
    genres TEXT,             

    -- RATINGS
    imdb_rating REAL,
    user_rating REAL,
    tmdb_rating REAL,
    tmdb_votes INTEGER,
    imdb_votes INTEGER,
    rotten_tomatoes TEXT,
    metascore INTEGER,

    -- IDs
    imdb_id TEXT,
    tmdb_id INTEGER,

    -- CREW & CAST
    director TEXT,
    cast TEXT,               

    -- MISC
    trailer TEXT,
    section TEXT DEFAULT 'want to watch',
    last_update TEXT,
    created_at TEXT DEFAULT (datetime('now'))
);


-- ================================
-- SERIES TABLE
-- ================================
CREATE TABLE IF NOT EXISTS series (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    year INTEGER,
    total_seasons INTEGER,
    episodes_json TEXT,         -- {"1":10,"2":12,"3":25}
    imdb_rating REAL,
    user_rating REAL,
    poster_path TEXT,
    genres TEXT,
    plot TEXT,
    imdb_id TEXT,
    tmdb_id INTEGER,
    last_update TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    section TEXT DEFAULT 'want to watch'
);

-- ================================
-- GAMES TABLE
-- ================================
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    year INTEGER,
    platform TEXT,
    genres TEXT,
    rating REAL,
    user_rating REAL,
    poster_path TEXT,
    plot TEXT,
    igdb_id TEXT,
    last_update TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    section TEXT DEFAULT 'want to play'
);

-- ================================
-- MANGA / COMICS TABLE
-- ================================
CREATE TABLE IF NOT EXISTS manga (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    chapters INTEGER,
    volumes INTEGER,
    status TEXT,                -- ongoing / completed
    poster_path TEXT,
    genres TEXT,
    plot TEXT,
    mal_id TEXT,
    user_rating REAL,
    last_update TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    section TEXT DEFAULT 'reading'
);

-- ================================
-- BOOKS TABLE
-- ================================
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    pages INTEGER,
    year INTEGER,
    genres TEXT,
    poster_path TEXT,
    plot TEXT,
    isbn TEXT,
    user_rating REAL,
    last_update TEXT,
    created_at TEXT DEFAULT (datetime('now')),
    section TEXT DEFAULT 'reading'
);
"""

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "movies.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the database and create tables if not exist."""
    with get_conn() as conn:
        conn.executescript(SCHEMA)

