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
        movie.runtime,
        movie.plot,
        movie.poster_path,

        json.dumps(movie.genres) if movie.genres else None,

        # ratings
        movie.imdb_rating,
        movie.user_rating,
        movie.tmdb_rating,
        movie.tmdb_votes,
        movie.imdb_votes,
        movie.rotten_tomatoes,
        movie.metascore,

        # ids
        movie.imdb_id,
        movie.tmdb_id,

        # crew & cast
        movie.director,
        json.dumps(movie.cast) if movie.cast else None,

        # misc
        movie.trailer,
        movie.section,
        movie.last_update,
    )


def row_to_movie(row):
    """Convert a database row into a Movie object."""
    return Movie(
        id=row["id"],
        title=row["title"],
        year=row["year"],
        runtime=row["runtime"],
        plot=row["plot"],
        poster_path=row["poster_path"],

        genres=json.loads(row["genres"]) if row["genres"] else [],

        imdb_rating=row["imdb_rating"],
        user_rating=row["user_rating"],
        tmdb_rating=row["tmdb_rating"],
        tmdb_votes=row["tmdb_votes"],
        imdb_votes=row["imdb_votes"],
        rotten_tomatoes=row["rotten_tomatoes"],
        metascore=row["metascore"],

        imdb_id=row["imdb_id"],
        tmdb_id=row["tmdb_id"],

        director=row["director"],
        cast=json.loads(row["cast"]) if row["cast"] else [],

        trailer=row["trailer"],
        section=row["section"],
        last_update=row["last_update"],
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
                title, year, runtime, plot, poster_path,
                genres,
                imdb_rating, user_rating, tmdb_rating, tmdb_votes,
                imdb_votes, rotten_tomatoes, metascore,
                imdb_id, tmdb_id,
                director, cast,
                trailer, section, last_update
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            UPDATE movies SET
                title = ?,
                year = ?,
                runtime = ?,
                plot = ?,
                poster_path = ?,

                genres = ?,

                imdb_rating = ?,
                user_rating = ?,
                tmdb_rating = ?,
                tmdb_votes = ?,
                imdb_votes = ?,
                rotten_tomatoes = ?,
                metascore = ?,

                imdb_id = ?,
                tmdb_id = ?,

                director = ?,
                cast = ?,

                trailer = ?,
                section = ?,
                last_update = ?

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

        query = f"""
        SELECT * FROM movies
        WHERE section = ?
        ORDER BY {order_by} {'DESC' if descending else 'ASC'}
        """

        cursor.execute(query, (section,))
        rows = cursor.fetchall()

    return [row_to_movie(row) for row in rows]


def move_movie_section(movie_id: int, new_section: str) -> bool:
    """Move a movie to another section."""
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
