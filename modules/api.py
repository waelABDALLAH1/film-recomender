import requests

API_KEY = "515bd4b0ba9dbfb9737341d5b8247e1d"

# Mappage des genres et des plateformes
genres = {"action": 28, "comédie": 35, "drame": 18, "aventure": 12}
providers = {"netflix": 8, "amazon prime": 119, "toutes": ""}

def fetch_movies(preferences):
    # Mapper les genres et plateformes
    preferences["genre"] = genres.get(preferences["genre"].lower(), "")
    preferences["plateforme"] = providers.get(preferences["plateforme"].lower(), "")

    # Construire l'URL et les paramètres
    url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": API_KEY,
        "language": "fr",
        "sort_by": "popularity.desc",
        "with_genres": preferences["genre"],
        "with_runtime.lte": preferences["durée"],
        "with_watch_providers": preferences["plateforme"],
        "watch_region": "FR"
    }

    # Appel API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # Afficher la réponse brute pour déboguer (facultatif)
        # print(response.json())
        return response.json().get("results", [])
    else:
        print(f"Erreur API : {response.status_code} - {response.text}")
        return []
