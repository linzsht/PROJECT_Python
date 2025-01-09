import matplotlib.pyplot as plt
import networkx as nx

# Création d'un graphe
G = nx.DiGraph()

# Ajout des nœuds pour les acteurs et cas d'utilisation
G.add_node("Utilisateur", shape="actor")
G.add_node("Rechercher Recettes")
G.add_node("Recherche Avancée")
G.add_node("Voir Statistiques")
G.add_node("API Spoonacular")

# Ajout des relations
G.add_edges_from([
    ("Utilisateur", "Rechercher Recettes"),
    ("Utilisateur", "Recherche Avancée"),
    ("Utilisateur", "Voir Statistiques"),
    ("Rechercher Recettes", "API Spoonacular"),
])

# Création de la disposition du graphe
pos = nx.spring_layout(G)

# Dessiner les nœuds
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="lightgreen", edgecolors="black")

# Dessiner les arêtes
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20)

# Ajouter les étiquettes
nx.draw_networkx_labels(G, pos, font_size=10)

# Afficher le graphe
plt.title("Diagramme d'Utilisation")
plt.axis("off")
plt.show()
