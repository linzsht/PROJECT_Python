import streamlit as st
import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Document import RecipeDocument
from Corpus import Corpus
from SearchEngine import SearchEngine
# Configuration de l'API Spoonacular
API_KEY = "34273252bf77435296c04da5fd660ed9"
BASE_URL = "https://api.spoonacular.com"

# Fonction pour nettoyer les balises HTML
import re
def clean_html(text):
    """Supprime les balises HTML du texte."""
    return re.sub(r'<[^>]+>', '', text)

# Fonction pour récupérer des recettes par mot-clé
def fetch_recipes(keyword, number_of_results=10):
    url = f"{BASE_URL}/recipes/complexSearch?query={keyword}&number={number_of_results}&apiKey={API_KEY}&addRecipeInformation=true"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        st.error("Erreur lors de la récupération des données.")
        return []

# Fonction pour créer des documents
def create_documents_from_recipes(recipes):
    documents = []
    for idx, recipe in enumerate(recipes):
        title = recipe.get('title', 'No Title')
        summary = clean_html(recipe.get('summary', 'No Summary'))
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

# Fonction principale pour rechercher des recettes
def fetch_and_save_recipes(keyword):
    recipes = fetch_recipes(keyword)
    if not recipes:
        return []
    documents = create_documents_from_recipes(recipes)
    return documents

# Streamlit interface
st.title("Recherche de Recettes et Analyse de Corpus")

# Étape 1 : Saisie du mot-clé pour les recettes
st.header("Étape 1 : Recherche de Recettes")
recipe_keyword = st.text_input("Entrez un mot-clé pour rechercher des recettes :")
if recipe_keyword:
    documents = fetch_and_save_recipes(recipe_keyword)
    if documents:
        st.success(f"{len(documents)} recettes récupérées avec succès !")
        corpus = Corpus(documents)

        # Affichage des recettes
        st.subheader("Recettes récupérées")
        for doc in documents:
            with st.expander(f"{doc.title}"):
                st.write(f"**Type de recette**: {doc.recipe_type}")
                st.write(f"**Source**: [Lien vers la recette]({doc.source})")
                st.write(f"**Temps de préparation**: {doc.ready_in_minutes} minutes")
                st.write(f"**Nombre de portions**: {doc.servings}")
                st.write(f"**Score de santé**: {doc.health_score}")
                st.write(f"**Extrait**: {doc.excerpt(200)}")

        # Étape 2 : Recherche dans le corpus
        st.header("Étape 2 : Recherche dans le Corpus")
        search_query = st.text_input("Entrez un mot-clé pour la recherche dans le corpus :")
        if search_query:
            search_results = corpus.search(search_query)
            if search_results:
                st.success(f"{len(search_results)} résultats trouvés dans le corpus.")
                for result in search_results:
                    with st.expander(f"{result.title}"):
                        st.write(f"**Extrait**: {result.excerpt(200)}")
            else:
                st.warning("Aucun résultat trouvé dans le corpus.")

        # Étape 3 : Recherche avancée avec moteur
        st.header("Étape 3 : Recherche Avancée")
        search_engine = SearchEngine(corpus)
        advanced_query = st.text_input("Entrez un mot-clé pour la recherche avancée avec score :")
        if advanced_query:
            advanced_results = search_engine.search(advanced_query)
            if advanced_results:
                st.success(f"{len(advanced_results)} résultats avancés trouvés.")
                for doc, score in advanced_results:
                    with st.expander(f"{doc.title} - Score: {score:.4f}"):
                        st.write(f"**Type de recette**: {doc.recipe_type}")
                        st.write(f"**Source**: [Lien vers la recette]({doc.source})")
                        st.write(f"**Temps de préparation**: {doc.ready_in_minutes} minutes")
                        st.write(f"**Nombre de portions**: {doc.servings}")
                        st.write(f"**Score de santé**: {doc.health_score}")
                        st.write(f"**Extrait**: {doc.excerpt(200)}")
            else:
                st.warning("Aucun résultat avancé trouvé.")
    else:
        st.warning("Aucune recette trouvée.")
