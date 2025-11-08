import os
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
import hashlib

# ------------------------------------------------------------------
# 🌐 Global network manager & cache
# ------------------------------------------------------------------
network_manager = QNetworkAccessManager()
memory_cache = {}  # {url_hash: QPixmap}

# Folder for disk caching
CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "posters")
os.makedirs(CACHE_DIR, exist_ok=True)


def _get_cache_path(url: str) -> str:
    """Return a filesystem path for cached image based on URL hash."""
    hash_name = hashlib.sha1(url.encode("utf-8")).hexdigest()
    return os.path.join(CACHE_DIR, f"{hash_name}.jpg")


def link_to_image(path: str, label, x: int, y: int):
    """Asynchronously load an image from URL with memory+disk caching."""
    if not path:
        label.setText("N/A")
        return

    # Generate cache key and file path
    cache_key = hashlib.sha1(path.encode()).hexdigest()
    cache_path = _get_cache_path(path)

    # 1️⃣ Check memory cache first
    if cache_key in memory_cache:
        _set_label_pixmap(label, memory_cache[cache_key], x, y)
        return

    # 2️⃣ Check disk cache next
    if os.path.exists(cache_path):
        pixmap = QPixmap(cache_path)
        if not pixmap.isNull():
            memory_cache[cache_key] = pixmap
            _set_label_pixmap(label, pixmap, x, y)
            return

    # 3️⃣ Otherwise, download asynchronously
    label.setText("Loading...")
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("color: gray; font-size: 10px; background-color: #222;")

    url = QUrl(path)
    if not url.isValid():
        label.setText("❌ Invalid URL")
        return

    request = QNetworkRequest(url)
    request.setRawHeader(b"User-Agent", b"Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    request.setAttribute(
        QNetworkRequest.Attribute.RedirectPolicyAttribute,
        QNetworkRequest.RedirectPolicy.NoLessSafeRedirectPolicy,
    )

    reply = network_manager.get(request)

    def on_image_loaded():
        if reply.error() != QNetworkReply.NetworkError.NoError:
            label.setText("⚠️ Error loading")
            reply.deleteLater()
            return

        data = reply.readAll()
        pixmap = QPixmap()
        if pixmap.loadFromData(data):
            # ✅ Cache both in memory and on disk
            memory_cache[cache_key] = pixmap
            pixmap.save(cache_path, "JPG")
            _set_label_pixmap(label, pixmap, x, y)
        else:
            label.setText("⚠️ Failed to decode image")

        reply.deleteLater()

    reply.finished.connect(on_image_loaded)


def _set_label_pixmap(label, pixmap: QPixmap, x: int, y: int):
    """Helper to scale and set pixmap safely."""
    scaled = pixmap.scaled(x, y, Qt.AspectRatioMode.KeepAspectRatio,
                           Qt.TransformationMode.SmoothTransformation)
    label.setPixmap(scaled)




def get_movie_by_id(data, section, movie_id):
    "ٌReturn a movie info using its section and id "
    movies = data.get(section, [])
    for movie in movies:
        if movie.get("id") == movie_id:
            return movie
    return None



def get_selected_section(combo_box):
    "Return section name in the combobox"
    index = combo_box.currentIndex()
    if index == -1:  # -1 means no selection
        return None
    text = combo_box.currentText().replace(" ", "_").lower()
    if not text:  # handle empty text too
        return None
    return text


def resize_combo_box_to_contents(combo):
    "resise the combobox to  see the full title on it"
    width = max(combo.fontMetrics().horizontalAdvance(combo.itemText(i)) for i in range(combo.count())) + 30
    combo.view().setMinimumWidth(width)


