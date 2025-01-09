from Document import Document, RecipeDocument
from Corpus import Corpus
from SearchEngine import SearchEngine
import pandas as pd

# Chargement des données
df = pd.read_csv('corpus_recipes.csv', sep='\t')
documents = [RecipeDocument(row['ID'], row['Text'], row['Text'], row['Source'], "Vegetarian" if "salad" in row['Text'].lower() else "Non-Vegetarian") for index, row in df.iterrows()]

# Création du corpus
corpus = Corpus(documents)

# Affichage de quelques statistiques et résultats de recherche
print(corpus.stats())
print(corpus.search("pasta"))
print(corpus.concorde("pasta"))

# Instanciation et utilisation du moteur de recherche
search_engine = SearchEngine(corpus)



query = input("Entrez quelques mots-clés pour la recherche: ")
results = search_engine.search(query)
print("Résultats de recherche:")

for doc, score in results:
    print(f"Titre: {doc.title}, Score: {score:.4f}")
    print(f"Texte: {doc.text[:49]}...")  # Afficher les premiers 49 caractères du texte
    print("-" * 50)

