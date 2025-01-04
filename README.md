# Générateur de recommandations de films et séries 🎥🍿

Ce projet est un script Python qui permet de générer des recommandations de films et séries basées sur vos préférences personnelles. Plus besoin de passer des heures à chercher quoi regarder, laissez Python faire le travail pour vous !

---

## Fonctionnalités 🛠️

- **Recommandations personnalisées** :
  - Sélectionnez le genre (action, comédie, drame, etc.).
  - Définissez une durée maximale (en minutes).
  - Choisissez la plateforme (Netflix, Amazon Prime, ou toutes).
- **Recommandations basées sur la popularité** :
  - Les suggestions sont triées par note et popularité.
- **Notifications** (optionnel) :
  - Recevez une alerte lorsqu’une nouvelle saison de vos séries préférées est disponible.
- **Suivi des films et séries regardés** :
  - Gardez une trace des épisodes et films déjà visionnés.

---

## Installation avec environnement virtuel 💻

### Prérequis
1. **Python 3.7+** installé sur votre machine.
2. Clé API TMDb (inscrivez-vous gratuitement ici : [TMDb](https://www.themoviedb.org/)).

### Étapes
1. **Clonez le projet** :
   ```bash
   git clone https://github.com/votre-utilisateur/film_recommender.git
   cd film_recommender
2.**Créez un environnement virtuel :
python -m venv myenv
3.Activez l’environnement virtuel :
source myenv/bin/activate
4.Installez les dépendances dans l’environnement virtuel :
pip install -r requirements.txt
5.Ajoutez votre clé API TMDb dans le fichier modules/api.py :
API_KEY = "votre_clé_API"
Utilisation
Pour lancer le générateur de recommandations, exécutez le fichier main.py :
python main.py


