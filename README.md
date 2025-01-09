# Projet de Recherche et Analyse de Recettes

Ce projet propose une application interactive permettant de rechercher, analyser et afficher des recettes culinaires en utilisant l'API **Spoonacular**. Il inclut un moteur de recherche avancé, une interface utilisateur développée avec **Streamlit**, et des fonctionnalités pour traiter et analyser les données des recettes.

## Fonctionnalités Principales
- Recherche de recettes via l'API Spoonacular.
- Nettoyage et structuration des données.
- Moteur de recherche basé sur **TF-IDF**.
- Interface interactive avec **Streamlit**.

---

## Prérequis
1. **Python 3.10** ou une version supérieure doit être installé sur votre machine.
2. **pip** (gestionnaire de paquets Python) doit être configuré.

---

## Installation

### 1. Cloner le Repository
Commencez par cloner le projet depuis GitHub :
```bash
git clone https://github.com/<votre-utilisateur>/<votre-repository>.git
cd <votre-repository>

### 2. Créer un Environnement Virtuel
Créez un environnement virtuel pour isoler les dépendances :
```bash
python -m venv venv

### 3. Activer l'Environnement Virtuel
- **Sous Windows** :
  ```bash
  venv\Scripts\activate

### 4. Lancer l'Application
Pour démarrer l'application Streamlit et accéder à l'interface utilisateur, utilisez la commande suivante :
streamlit run app.py

