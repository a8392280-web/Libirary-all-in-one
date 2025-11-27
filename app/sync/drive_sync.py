import os
from pathlib import Path
from datetime import datetime, timezone
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from app.db.sqlite_manger import init_db

def build_drive_service(credentials):
    return build("drive", "v3", credentials=credentials, cache_discovery=False)


def find_db_file(service, filename: str):
    """Check if file exists in appDataFolder."""
    try:
        res = service.files().list(
            spaces="appDataFolder",
            q=f"name='{filename}' and trashed = false",
            fields="files(id, name, modifiedTime)"
        ).execute()
        files = res.get("files", [])
        return files[0] if files else None
    except Exception as e:
        print(f"[find_db_file] Error: {e}")
        return None


def download_db(service, file_id: str, local_path: str):
    """Download file from Drive to local path."""
    try:
        request = service.files().get_media(fileId=file_id)
        Path(local_path).parent.mkdir(parents=True, exist_ok=True)
        with open(local_path, "wb") as fh:
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                _, done = downloader.next_chunk()
        return local_path
    except Exception as e:
        print(f"[download_db] Error: {e}")
        return None


def upload_db(service, local_path: str, filename: str):
    """Upload local DB to Drive; update if exists."""
    try:
        existing = find_db_file(service, filename)
        media = MediaFileUpload(local_path, mimetype="application/x-sqlite3", resumable=True)
        if existing:
            request = service.files().update(fileId=existing["id"], media_body=media)
        else:
            file_metadata = {"name": filename, "parents": ["appDataFolder"]}
            request = service.files().create(body=file_metadata, media_body=media, fields="id")

        response = None
        while response is None:
            _, response = request.next_chunk()
        return response
    except Exception as e:
        print(f"[upload_db] Error: {e}")
        return None


def parse_google_time(gtime: str):
    return datetime.fromisoformat(gtime.replace("Z", "+00:00"))


def sync_on_login(credentials, local_path: str, filename: str = "movies.db"):
    """Sync local DB with Drive on login."""
    try:
        service = build_drive_service(credentials)
        remote = find_db_file(service, filename)
        local_exists = os.path.exists(local_path)

        if remote:
            remote_time = parse_google_time(remote["modifiedTime"])
            local_time = datetime.fromtimestamp(os.path.getmtime(local_path), tz=timezone.utc) if local_exists else None
            if not local_exists:
                download_db(service, remote["id"], local_path)
                return "downloaded"

        else:
            if not local_exists:
                init_db()
                return "Fresh DB"

    except Exception as e:
        print(f"[sync_on_login] Failed to sync: {e}")
        if not local_exists:
            init_db()
            return "Fresh DB"
        return "error"