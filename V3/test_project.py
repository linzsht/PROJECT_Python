import unittest
from Document import Document, RecipeDocument
from Corpus import Corpus
from SearchEngine import SearchEngine
from T3 import clean_html, create_documents_from_recipes
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class TestDocument(unittest.TestCase):
    def test_document_initialization(self):
        doc = Document(1, "Test Title", "Test Text", "Test Source")
        self.assertEqual(doc.id, 1)
        self.assertEqual(doc.title, "Test Title")
        self.assertEqual(doc.text, "Test Text")
        self.assertEqual(doc.source, "Test Source")
    
    def test_contains_keyword(self):
        doc = Document(1, "Title", "This is a test text", "Source")
        self.assertTrue(doc.contains_keyword("test"))
        self.assertFalse(doc.contains_keyword("missing"))

class TestRecipeDocument(unittest.TestCase):
    def test_recipe_document_initialization(self):
        recipe = RecipeDocument(1, "Recipe", "Text", "Source", "Vegetarian", 30, 4, 80)
        self.assertEqual(recipe.recipe_type, "Vegetarian")
        self.assertEqual(recipe.ready_in_minutes, 30)
        self.assertEqual(recipe.servings, 4)
        self.assertEqual(recipe.health_score, 80)

class TestCorpus(unittest.TestCase):
    def setUp(self):
        self.documents = [
            Document(1, "Doc1", "Text about pasta.", "Source1"),
            Document(2, "Doc2", "Another text about pasta.", "Source2"),
            Document(3, "Doc3", "No pasta here.", "Source3")
        ]
        self.corpus = Corpus(self.documents)

    def test_search(self):
        results = self.corpus.search("pasta")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].title, "Doc1")

    def test_stats(self):
        stats = self.corpus.stats()
        self.assertTrue(("pasta", 2) in stats)

class TestSearchEngine(unittest.TestCase):
    def setUp(self):
        self.documents = [
            Document(1, "Doc1", "Pasta recipe.", "Source1"),
            Document(2, "Doc2", "Healthy salad recipe.", "Source2")
        ]
        self.corpus = Corpus(self.documents)
        self.search_engine = SearchEngine(self.corpus)

    def test_search(self):
        results = self.search_engine.search("pasta")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0].title, "Doc1")

class TestT3(unittest.TestCase):
    def test_clean_html(self):
        html_text = "<p>This is a <b>test</b>.</p>"
        cleaned_text = clean_html(html_text)
        self.assertEqual(cleaned_text, "This is a test.")

    def test_create_documents_from_recipes(self):
        recipes = [
            {
                "title": "Recipe1",
                "summary": "<p>Healthy and delicious.</p>",
                "sourceUrl": "http://example.com",
                "vegetarian": True,
                "readyInMinutes": 20,
                "servings": 4,
                "healthScore": 90
            }
        ]
        documents = create_documents_from_recipes(recipes)
        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0].title, "Recipe1")
        self.assertEqual(documents[0].ready_in_minutes, 20)

if __name__ == "__main__":
    unittest.main()
