import matplotlib.pyplot as plt
import networkx as nx

# Création d'un graphe
G = nx.DiGraph()

# Ajout des nœuds pour les classes
G.add_node("Document", label="Document\n- id, title, text, source\n+ contains_keyword()")
G.add_node("RecipeDocument", label="RecipeDocument\n- ready_in_minutes, servings\n+ __str__()")
G.add_node("Corpus", label="Corpus\n- documents, all_text\n+ search(), stats()")
G.add_node("SearchEngine", label="SearchEngine\n- vectorizer, tfidf_matrix\n+ search()")
G.add_node("API", label="Spoonacular API")

# Ajout des relations entre les classes
G.add_edges_from([
    ("RecipeDocument", "Document"),  # Héritage
    ("Corpus", "RecipeDocument"),   # Composition
    ("SearchEngine", "Corpus"),     # Utilisation
    ("RecipeDocument", "API"),      # Dépendance avec API
])

# Création de la disposition du graphe
pos = nx.spring_layout(G)

# Dessiner les nœuds
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="lightblue", edgecolors="black")

# Dessiner les arêtes
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20)

# Ajouter les étiquettes
labels = nx.get_node_attributes(G, "label")
nx.draw_networkx_labels(G, pos, labels={n: n for n in G.nodes}, font_size=10)

# Afficher le graphe
plt.title("Diagramme de Classes")
plt.axis("off")
plt.show()
