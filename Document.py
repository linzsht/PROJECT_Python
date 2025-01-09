class Document:
    def __init__(self, id, title, text, source,author=None, date=None, summary=None):
        self.id = id
        self.title = title
        self.text = text
        self.source = source
        self.author = author
        self.date = date
        self.summary = summary

    def __str__(self):
        return f"{self.title} by {self.author} on {self.date}"
    
    def excerpt(self, length=150):
        """Returns the first 'length' characters of the document text followed by '...' if longer."""
        return self.text[:length] + "..." if len(self.text) > length else self.text
    def contains_keyword(self, keyword):
        """Check if the document contains the given keyword."""
        return keyword.lower() in self.text.lower()
class RecipeDocument(Document):
    def __init__(self, id, title, text, source, recipe_type, ready_in_minutes=None, servings=None, health_score=None):
        super().__init__(id, title, text, source)
        self.recipe_type = recipe_type
        self.ready_in_minutes = ready_in_minutes
        self.servings = servings
        self.health_score = health_score

    def __str__(self):
        return super().__str__() + f" - Type: {self.recipe_type}"
