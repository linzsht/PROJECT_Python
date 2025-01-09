from Document import RecipeDocument
from Corpus import Corpus
from SearchEngine import SearchEngine
import pandas as pd
from T3 import fetch_and_save_recipes

# Récupération des documents à partir de l'API et création du corpus
documents = fetch_and_save_recipes()
if documents:
    # Création du corpus
    corpus = Corpus(documents)

    # Affichage des statistiques
    print("Statistiques du corpus:", corpus.stats())

    # Recherche dans le corpus
    query = input("Entrez des mots-clés pour la recherche: ")
    results = corpus.search(query)
    print("\nRésultats de la recherche dans le corpus:")
    for result in results:
        print(f"Titre: {result.title}, Extrait: {result.excerpt(50)}")

    # Instanciation et utilisation du moteur de recherche
    search_engine = SearchEngine(corpus)
    query = input("\nRecherche avancée avec score: ")
    results = search_engine.search(query)
    print("\nRésultats de la recherche avancée:")
    for doc, score in results:
        print(f"Titre: {doc.title}, Score: {score:.4f}")
else:
    print("Aucun document à traiter.")