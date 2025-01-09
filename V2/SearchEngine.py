from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from Document import Document
import numpy as np
from Corpus import Corpus

class SearchEngine:
    def __init__(self, corpus):
        self.corpus = corpus
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform([doc.text for doc in corpus.documents])

    def search(self, query, n_results=5):
        query_vec = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        related_docs_indices = cosine_similarities.argsort()[:-n_results-1:-1]
        return [(self.corpus.documents[index], cosine_similarities[index]) for index in related_docs_indices]



