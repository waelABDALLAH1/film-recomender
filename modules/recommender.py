def filter_recommendations(movies):
    recommendations = []
    for movie in movies:
        recommendations.append({
            "titre": movie.get("title", "Titre inconnu"),
            "note": movie.get("vote_average", 0),
            "date_sortie": movie.get("release_date", "Date inconnue"),
            "description": movie.get("overview", "Pas de description")
        })
    return recommendations
