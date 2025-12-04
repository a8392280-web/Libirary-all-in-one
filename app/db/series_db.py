# app/db/series_db.py
from app.models.series import Series
from app.db.sqlite_manger import get_conn
import json
import sqlite3

# ==========================================================
# 🔄 CONVERSION HELPERS
# ==========================================================
def series_to_tuple(series: Series):
    """Convert a Series object into a tuple for SQL insertion."""
    return (
        series.title,
        series.year,
        series.runtime,

        series.total_seasons,
        series.total_episodes,
        json.dumps(series.seasons) if series.seasons else None,

        json.dumps(series.genres) if series.genres else None,
        series.plot,
        series.creator,
        json.dumps(series.cast) if series.cast else None,

        series.tmdb_id,
        series.imdb_id,

        series.user_rating,
        series.tmdb_rating,
        series.tmdb_votes,
        series.imdb_rating,
        series.imdb_votes,
        series.metascore,
        series.rotten_tomatoes,

        series.trailer,
        series.poster_path,
        series.section,
        series.last_update,
    )


def row_to_series(row):
    """Convert a database row into a Series object."""
    return Series(
        id=row["id"],
        title=row["title"],
        year=row["year"],
        runtime=row["runtime"],

        total_seasons=row["total_seasons"],
        total_episodes=row["total_episodes"],
        seasons=json.loads(row["seasons"]) if row["seasons"] else [],

        genres=json.loads(row["genres"]) if row["genres"] else [],
        plot=row["plot"],
        creator=row["creator"],
        cast=json.loads(row["cast"]) if row["cast"] else [],

        tmdb_id=row["tmdb_id"],
        imdb_id=row["imdb_id"],

        user_rating=row["user_rating"],
        tmdb_rating=row["tmdb_rating"],
        tmdb_votes=row["tmdb_votes"],
        imdb_rating=row["imdb_rating"],
        imdb_votes=row["imdb_votes"],
        metascore=row["metascore"],
        rotten_tomatoes=row["rotten_tomatoes"],

        trailer=row["trailer"],
        poster_path=row["poster_path"],
        section=row["section"],
        last_update=row["last_update"],
    )


# ==========================================================
# 🟢 CRUD OPERATIONS
# ==========================================================
def insert_series(series: Series):
    """Insert a new series into the database."""
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO series (
                title, year, runtime,
                total_seasons, total_episodes, seasons,
                genres, plot, creator, cast,
                tmdb_id, imdb_id,
                user_rating, tmdb_rating, tmdb_votes, imdb_rating, imdb_votes,
                metascore, rotten_tomatoes,
                trailer, poster_path, section, last_update
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
            """,
            series_to_tuple(series)
        )
        series.id = cursor.lastrowid
    return series


def update_series(series: Series):
    """Update an existing series."""
    if series.id is None:
        raise ValueError("Series must have an ID to update")

    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE series SET
                title = ?, year = ?, runtime = ?,
                total_seasons = ?, total_episodes = ?, seasons = ?,
                genres = ?, plot = ?, creator = ?, cast = ?,
                tmdb_id = ?, imdb_id = ?,
                user_rating = ?, tmdb_rating = ?, tmdb_votes = ?, imdb_rating = ?, imdb_votes = ?,
                metascore = ?, rotten_tomatoes = ?,
                trailer = ?, poster_path = ?, section = ?, last_update = ?
            WHERE id = ?
            """,
            series_to_tuple(series) + (series.id,)
        )
    return series


def delete_series(series_id: int) -> int:
    """Delete a series by ID."""
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM series WHERE id = ?", (series_id,))
        return cursor.rowcount


def get_series_by_id(series_id: int) -> Series | None:
    """Fetch a single series by ID."""
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM series WHERE id = ?", (series_id,))
        row = cursor.fetchone()
        return row_to_series(row) if row else None


# ==========================================================
# 🔍 QUERY UTILITIES
# ==========================================================
def list_series(section: str, order_by: str = "title", descending: bool = False):
    """Fetch series filtered by section and sorted."""
    if not section:
        raise ValueError("Section must be provided")

    with get_conn() as conn:
        cursor = conn.cursor()

        query = f"""
        SELECT * FROM series
        WHERE section = ?
        ORDER BY {order_by} {'DESC' if descending else 'ASC'}
        """

        cursor.execute(query, (section,))
        rows = cursor.fetchall()

    return [row_to_series(row) for row in rows]


def move_series_section(series_id: int, new_section: str) -> bool:
    """Move a series to another section."""
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE series SET section = ?, last_update = datetime('now') WHERE id = ?",
            (new_section, series_id)
        )
        return cursor.rowcount > 0


def count_series(section: str) -> int:
    """Count how many series exist in a specific section."""
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM series WHERE section = ?", (section,))
        return cursor.fetchone()[0]
