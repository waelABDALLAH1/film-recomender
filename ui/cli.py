from modules.api import fetch_movies
from modules.recommender import filter_recommendations

def start_cli():
    # Collecte des préférences utilisateur
    genre = input("Entrez le genre (ex: action, comédie) : ")
    durée = input("Entrez la durée maximale (en minutes, ex: 120) : ")
    plateforme = input("Entrez la plateforme (Netflix, Amazon Prime ou toutes) : ")
    preferences = {"genre": genre, "durée": durée, "plateforme": plateforme}

    # Appel à l'API
    print("\nRecherche en cours...")
    movies = fetch_movies(preferences)

    # Traitement des résultats
    recommendations = filter_recommendations(movies)

    # Affichage des recommandations
    print("\nVoici vos recommandations :")
    for movie in recommendations[:10]:  # Limite à 10 films
        print(f"- {movie['titre']} ({movie['date_sortie'][:4]}) - Note : {movie['note']}")
