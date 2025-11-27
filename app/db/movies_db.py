from app.models.movie import Movie
from app.db.sqlite_manger import get_conn
import json
import sqlite3

# ==========================================================
# 🔄 CONVERSION HELPERS
# ==========================================================
def movie_to_tuple(movie: Movie):
    """Convert a Movie object into a tuple for SQL insertion."""
    return (
        movie.title,
        movie.year,
        movie.rating,
        movie.user_rating,
        movie.runtime,
        movie.poster_path,
        json.dumps(movie.genres) if movie.genres else None,
        movie.plot,
        movie.imdb_id,
        movie.tmdb_id,
        movie.last_update,
        movie.section,
        movie.trailer
    )


def row_to_movie(row):
    """Convert a database row into a Movie object."""
    return Movie(
        id=row["id"],
        title=row["title"],
        year=row["year"],
        rating=row["rating"],
        user_rating=row["user_rating"],
        runtime=row["runtime"],
        poster_path=row["poster_path"],
        genres=json.loads(row["genres"]) if row["genres"] else [],
        plot=row["plot"],
        imdb_id=row["imdb_id"],
        tmdb_id=row["tmdb_id"],
        last_update=row["last_update"],
        section=row["section"],
        trailer=row["trailer"]
    )


# ==========================================================
# 🟢 CRUD OPERATIONS
# ==========================================================
def insert_movie(movie: Movie):
    """Insert a new movie into the database."""
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO movies (
                title, year, rating, user_rating, runtime,
                poster_path, genres, plot, imdb_id, tmdb_id, last_update, section, trailer
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            movie_to_tuple(movie)
        )
        movie.id = cursor.lastrowid

    return movie


def update_movie(movie: Movie):
    """Update an existing movie by ID."""
    if movie.id is None:
        raise ValueError("Movie must have an ID to update")

    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE movies
            SET title = ?,
                year = ?,
                rating = ?,
                user_rating = ?,
                runtime = ?,
                poster_path = ?,
                genres = ?,
                plot = ?,
                imdb_id = ?,
                tmdb_id = ?,
                last_update = ?,
                section = ?,
                trailer = ?
            WHERE id = ?
            """,
            movie_to_tuple(movie) + (movie.id,)
        )
    return movie


def delete_movie(movie_id: int) -> int:
    """Delete a movie by ID. Returns number of rows deleted."""
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
        return cursor.rowcount


def get_movie_by_id(movie_id: int) -> Movie | None:
    """Fetch a single movie by its ID."""
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
        row = cursor.fetchone()
        return row_to_movie(row) if row else None


# ==========================================================
# 🔍 QUERY UTILITIES
# ==========================================================
def list_movies(section: str, order_by: str = "title", descending: bool = False):
    """Fetch movies filtered by section and sorted."""
    if not section:
        raise ValueError("Section must be provided")

    with get_conn() as conn:
        cursor = conn.cursor()
        query = f"SELECT * FROM movies WHERE section = ? ORDER BY {order_by} {'DESC' if descending else 'ASC'}"
        cursor.execute(query, (section,))
        rows = cursor.fetchall()

    return [row_to_movie(row) for row in rows]




def move_movie_section(movie_id: int, new_section: str) -> bool:
    """Move a movie to another section (e.g., watching → watched)."""
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE movies SET section = ?, last_update = datetime('now') WHERE id = ?",
            (new_section, movie_id)
        )
        return cursor.rowcount > 0


def count_movies(section: str) -> int:
    """Count how many movies exist in a specific section."""
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM movies WHERE section = ?", (section,))
        return cursor.fetchone()[0]
