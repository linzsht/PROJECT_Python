class Document:
    def __init__(self, id, title, text, source):
        self.id = id
        self.title = title
        self.text = text
        self.source = source

    def __str__(self):
        return f"{self.title} from {self.source}"

class RecipeDocument(Document):
    def __init__(self, id, title, text, source, recipe_type):
        super().__init__(id, title, text, source)
        self.recipe_type = recipe_type

    def __str__(self):
        return super().__str__() + f" - Type: {self.recipe_type}"