import requests
import pandas as pd

# Configuration de l'API Spoonacular
API_KEY = "34273252bf77435296c04da5fd660ed9"
BASE_URL = "https://api.spoonacular.com"

# Fonction pour récupérer des recettes par mot-clé
def fetch_recipes(keyword, number_of_results=100):
    url = f"{BASE_URL}/recipes/complexSearch?query={keyword}&number={number_of_results}&apiKey={API_KEY}&addRecipeInformation=true"
    response = requests.get(url)
    return response.json()['results']

# Récupération des recettes pour une thématique
keyword = "pasta"
recipes = fetch_recipes(keyword)

# Construction du corpus
corpus = []
for recipe in recipes:
    text = recipe['title'] + ". " + (recipe['summary'] if 'summary' in recipe else "")
    corpus.append(text)

# Sauvegarde des données dans un DataFrame
import pandas as pd
df = pd.DataFrame(corpus, columns=['Text'])
df['ID'] = range(1, len(df) + 1)
df['Source'] = 'Spoonacular'
df.to_csv('corpus_recipes.csv', sep='\t', index=False)

# Chargement des données sans appel API
loaded_df = pd.read_csv('corpus_recipes.csv', sep='\t')
print(loaded_df.head())
