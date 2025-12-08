from app.models.movie import Movie, MOVIE_COLUMNS
from app.db.sqlite_manger import get_conn
import json

# ==========================================================
# 🔄 CONVERSION HELPERS
# ==========================================================

def movie_to_tuple(movie: Movie):
    """Convert Movie object into a tuple dynamically."""
    values = []
    for col in MOVIE_COLUMNS:
        value = getattr(movie, col, None)
        if isinstance(value, (list, dict)):
            value = json.dumps(value)
        values.append(value)
    return tuple(values)

def row_to_movie(row):
    """Convert a DB row into a Movie object dynamically."""
    data = {}
    for col in MOVIE_COLUMNS:
        value = row[col]
        if col in ["genres", "cast"] and value:
            value = json.loads(value)
        data[col] = value
    return Movie(**data, id=row["id"])



# ==========================================================
# 🟢 CRUD OPERATIONS
# ==========================================================
def insert_movie(movie: Movie):
    cols = ", ".join(MOVIE_COLUMNS)
    placeholders = ", ".join(["?"] * len(MOVIE_COLUMNS))
    values = movie_to_tuple(movie)

    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO movies ({cols}) VALUES ({placeholders})", values)
        movie.id = cursor.lastrowid
    return movie

def update_movie(movie: Movie):
    if movie.id is None:
        raise ValueError("Movie must have an ID to update")

    set_clause = ", ".join(f"{col}=?" for col in MOVIE_COLUMNS)
    values = movie_to_tuple(movie) + (movie.id,)

    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE movies SET {set_clause} WHERE id=?", values)
    return movie

def delete_movie(movie_id: int) -> int:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM movies WHERE id=?", (movie_id,))
        return cursor.rowcount

def get_movie_by_id(movie_id: int) -> Movie | None:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movies WHERE id=?", (movie_id,))
        row = cursor.fetchone()
        return row_to_movie(row) if row else None


# ==========================================================
# 🔍 QUERY UTILITIES
# ==========================================================
def list_movies(section: str, order_by: str = "title", descending: bool = False):
    if not section:
        raise ValueError("Section must be provided")

    with get_conn() as conn:
        cursor = conn.cursor()
        query = f"""
        SELECT * FROM movies
        WHERE section=?
        ORDER BY {order_by} {'DESC' if descending else 'ASC'}
        """
        cursor.execute(query, (section,))
        rows = cursor.fetchall()

    return [row_to_movie(row) for row in rows]

def move_movie_section(movie_id: int, new_section: str) -> bool:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE movies SET section=?, last_update=datetime('now') WHERE id=?",
            (new_section, movie_id)
        )
        return cursor.rowcount > 0

def count_movies(section: str) -> int:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM movies WHERE section=?", (section,))
        return cursor.fetchone()[0]
