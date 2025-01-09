from Document import RecipeDocument
import pandas as pd
from Document import Document

df = pd.read_csv('corpus_recipes.csv', sep='\t')

documents = [RecipeDocument(row['ID'], row['Text'], row['Text'], row['Source'], "Vegetarian" if "salad" in row['Text'].lower() else "Non-Vegetarian") for index, row in df.iterrows()]

for doc in documents:
    print(doc)


df = pd.read_csv('corpus_recipes.csv', sep='\t')

documents = [Document(row['ID'], row['Text'], row['Text'], row['Source']) for index, row in df.iterrows()]

for doc in documents:
    print(doc)
