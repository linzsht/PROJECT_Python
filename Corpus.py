import re
from collections import Counter
from Document import RecipeDocument
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')

class Corpus:
    def __init__(self, documents):
        self.documents = documents
        self.all_text = " ".join(doc.text for doc in documents)
    def _clean_text(self, text):
        # Supprime les balises HTML
        text = re.sub(r'<[^>]+>', '', text)
        # Supprime les caractères non alphabétiques
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convertit en minuscules
        text = text.lower()
        # Supprime les stopwords
        stop_words = set(stopwords.words('english'))
        text = " ".join(word for word in text.split() if word not in stop_words)
        return text
    def search(self, keyword):
        return [doc for doc in self.documents if doc.contains_keyword(keyword)]

    def concorde(self, expression, context=30):
        pattern = re.compile(r".{0,%d}%s.{0,%d}" % (context, re.escape(expression)), re.IGNORECASE)
        results = []
        for doc in self.documents:
            for match in pattern.finditer(doc.text):
                results.append({
                    "document": doc,
                    "context": match.group(0)
                })
        return results

    def stats(self):
        words = re.findall(r'\w+', self.all_text.lower())
        frequency = Counter(words)
        return frequency.most_common(10)
