# app/db/series_db.py
from app.models.series import Series, SERIES_COLUMNS
from app.db.sqlite_manger import get_conn
import json


# ==========================================================
# 🔄 CONVERSION HELPERS
# ==========================================================
def series_to_tuple(series: Series):
    """Convert Series object into a tuple dynamically."""
    values = []
    for col in SERIES_COLUMNS:
        value = getattr(series, col, None)
        if isinstance(value, (list, dict)):
            value = json.dumps(value)
        values.append(value)
    return tuple(values)


def row_to_series(row):
    """Convert a DB row into a Series object dynamically."""
    data = {}
    for col in SERIES_COLUMNS:
        value = row[col]

        # JSON decode for list/dict fields
        if col in ["genres", "seasons", "cast"] and value:
            value = json.loads(value)

        data[col] = value

    return Series(**data, id=row["id"])


# ==========================================================
# 🟢 CRUD OPERATIONS
# ==========================================================
def insert_series(series: Series):
    cols = ", ".join(SERIES_COLUMNS)
    placeholders = ", ".join(["?"] * len(SERIES_COLUMNS))
    values = series_to_tuple(series)

    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO series ({cols}) VALUES ({placeholders})", values)
        series.id = cursor.lastrowid

    return series


def update_series(series: Series):
    if series.id is None:
        raise ValueError("Series must have an ID to update")

    set_clause = ", ".join(f"{col}=?" for col in SERIES_COLUMNS)
    values = series_to_tuple(series) + (series.id,)

    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE series SET {set_clause} WHERE id=?", values)

    return series


def delete_series(series_id: int) -> int:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM series WHERE id=?", (series_id,))
        return cursor.rowcount


def get_series_by_id(series_id: int) -> Series | None:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM series WHERE id=?", (series_id,))
        row = cursor.fetchone()
        return row_to_series(row) if row else None


# ==========================================================
# 🔍 QUERY UTILITIES
# ==========================================================
def list_series(section: str, order_by: str = "title", descending: bool = False):
    if not section:
        raise ValueError("Section must be provided")

    with get_conn() as conn:
        cursor = conn.cursor()

        query = f"""
        SELECT * FROM series
        WHERE section=?
        ORDER BY {order_by} {'DESC' if descending else 'ASC'}
        """

        cursor.execute(query, (section,))
        rows = cursor.fetchall()

    return [row_to_series(row) for row in rows]


def move_series_section(series_id: int, new_section: str) -> bool:
    with get_conn() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE series SET section=?, last_update=datetime('now') WHERE id=?",
            (new_section, series_id)
        )

        return cursor.rowcount > 0


def count_series(section: str) -> int:
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM series WHERE section=?", (section,))
        return cursor.fetchone()[0]
