from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Recommended scopes for user info
SCOPES = [
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/userinfo.email",
    "openid",
    "https://www.googleapis.com/auth/drive.appdata" 
]                                         



CREDENTIALS_FILE = Path.cwd() / "credentials.json"
TOKEN_FILE = Path.cwd() / "token.json"

class GoogleAuth:
    def __init__(self):
        self.creds = None

    def login(self):
        """Login via OAuth or refresh existing token."""
        # Try load saved token first
        if TOKEN_FILE.exists():
            self.creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
            if self.creds and self.creds.valid:
                return self.creds
            elif self.creds and self.creds.expired and self.creds.refresh_token:
                try:
                    print("[GoogleAuth] Refreshing expired token...")
                    self.creds.refresh(Request())
                    # Save refreshed token
                    TOKEN_FILE.write_text(self.creds.to_json(), encoding="utf-8")
                    return self.creds
                except Exception as e:
                    print(f"[GoogleAuth] Token refresh failed: {e}")
    def sign_in(self):
        # First-time login or refresh failed
        flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
        print(  "[GoogleAuth] Starting OAuth flow..."  )
        self.creds = flow.run_local_server(port=0)
        print(  "[GoogleAuth] OAuth flow completed."  )

        # Save token for next time
        # TOKEN_FILE.write_text(self.creds.to_json(), encoding="utf-8")
        # OR keep your original approach:
        with open(TOKEN_FILE, "w", encoding="utf-8") as f:
            f.write(self.creds.to_json())
            
        return self.creds


def get_user_info(creds):
    """Fetch logged-in user's info from Google."""
    try:
        service = build("oauth2", "v2", credentials=creds)
        user_info = service.userinfo().get().execute()
        return {
            "id": user_info.get("id"),
            "email": user_info.get("email"),
            "name": user_info.get("name"),
            "profile_pic": user_info.get("picture"),
        }
    except Exception as e:
        print(f"[get_user_info] Failed to fetch user info: {e}")
        return None
