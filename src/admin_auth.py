import json
from pathlib import Path

def load_admins():
    admins_path = Path(__file__).parent / "admins.json"
    if admins_path.exists():
        with open(admins_path, "r") as f:
            return json.load(f)
    return {}

def authenticate_admin(username, password):
    admins = load_admins()
    return admins.get(username) == password
