import requests
import pandas as pd
from Document import RecipeDocument  # Importer la classe RecipeDocument
import re

# Configuration de l'API Spoonacular
API_KEY = "34273252bf77435296c04da5fd660ed9"
BASE_URL = "https://api.spoonacular.com"

# Fonction pour récupérer des recettes par mot-clé
def fetch_recipes(keyword, number_of_results=100):
    url = f"{BASE_URL}/recipes/complexSearch?query={keyword}&number={number_of_results}&apiKey={API_KEY}&addRecipeInformation=true"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print("Erreur lors de la récupération des données :", response.status_code)
        return []

# Fonction pour créer des documents à partir des recettes
def clean_html(text):
    """Supprime les balises HTML du texte."""
    return re.sub(r'<[^>]+>', '', text)
def create_documents_from_recipes(recipes):
    documents = []
    for idx, recipe in enumerate(recipes):
        title = recipe.get('title', 'No Title')
        summary = recipe.get('summary', 'No Summary')
        summary = clean_html(summary)  # Nettoyage des balises HTML
        source = recipe.get('sourceUrl', 'No Source URL')
        ready_in_minutes = recipe.get('readyInMinutes', 'Unknown')
        servings = recipe.get('servings', 'Unknown')
        health_score = recipe.get('healthScore', 'Unknown')
        text = f"{title}. {summary}"
        recipe_type = "Vegetarian" if recipe.get('vegetarian', False) else "Non-Vegetarian"
        document = RecipeDocument(
            idx + 1, title, text, source, recipe_type,
            ready_in_minutes=ready_in_minutes,
            servings=servings,
            health_score=health_score
        )
        documents.append(document)
    return documents

# Fonction principale pour récupérer et sauvegarder les données
def fetch_and_save_recipes():
    keyword = input("Entrez un mot-clé pour rechercher des recettes: ")
    recipes = fetch_recipes(keyword)
    if not recipes:
        print("Aucune recette trouvée.")
        return []

    documents = create_documents_from_recipes(recipes)

    # Sauvegarde dans un fichier CSV
    df = pd.DataFrame([{
        'ID': doc.id,
        'Title': doc.title,
        'Text': doc.text,
        'Source': doc.source,
        'RecipeType': doc.recipe_type
    } for doc in documents])

    df.to_csv('corpus_recipes.csv', sep='\t', index=False)
    print("Les recettes ont été sauvegardées dans 'corpus_recipes.csv'")
    return documents
