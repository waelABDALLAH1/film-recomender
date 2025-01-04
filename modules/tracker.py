import json

TRACKING_FILE = "data/tracking.json"

def load_tracking():
    try:
        with open(TRACKING_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_tracking(data):
    with open(TRACKING_FILE, "w") as f:
        json.dump(data, f, indent=4)

def track_series(series_name, episode):
    tracking = load_tracking()
    tracking[series_name] = episode
    save_tracking(tracking)
    print(f"Suivi mis à jour : {series_name} - Épisode {episode}")
