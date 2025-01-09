import re
import pandas as pd
from collections import Counter
from Document import Document
class Corpus:
    def __init__(self, documents):
        self.documents = documents
        self.all_text = " ".join(doc.text for doc in documents)

    def search(self, keyword):
        return re.findall(r'\b{}\b'.format(re.escape(keyword)), self.all_text, re.IGNORECASE)

    def concorde(self, expression, context=30):
        pattern = r".{{0,{0}}}\b{1}\b.{{0,{0}}}".format(context, re.escape(expression))
        results = re.finditer(pattern, self.all_text, re.IGNORECASE)
        return [(result.group(0), result.start()) for result in results]

    def stats(self):
        words = re.findall(r'\w+', self.all_text.lower())
        frequency = Counter(words)
        return frequency.most_common(10)

# Ajout des méthodes à la classe Corpus
df = pd.read_csv('corpus_recipes.csv', sep='\t')

documents = [Document(row['ID'], row['Text'], row['Text'], row['Source']) for index, row in df.iterrows()]
corpus = Corpus(documents)  # Assurez-vous que 'documents' est une liste d'instances de Document
print(corpus.search("pasta"))
print(corpus.concorde("pasta", 10))
print(corpus.stats())
