# Guide d'utilisation - University Scholar

## 📋 Vue d'ensemble

Le module **University Scholar** permet de :
- Gérer les enseignants et leurs informations
- Importer automatiquement leurs articles depuis Google Scholar via SerpAPI
- Suivre les citations, H-index, et statistiques de publications

---

## 🚀 Étape 1 : Configuration initiale

### 1.1 Obtenir une clé API SerpAPI

1. Allez sur https://serpapi.com/
2. Créez un compte (gratuit avec quota limité)
3. Allez dans votre dashboard et récupérez votre **API Key**

### 1.2 Configurer la clé API dans Odoo

1. Dans Odoo, allez dans **Paramètres** (icône engrenage en haut à droite)
2. Cherchez la section **"University Scholar"**
3. Entrez votre clé API SerpAPI dans le champ **"SerpAPI Key"**
4. Cliquez sur **Sauvegarder**

---

## 👨‍🏫 Étape 2 : Créer un enseignant

### 2.1 Accéder au menu

1. Dans le menu principal, cliquez sur **"Université"**
2. Cliquez sur **"Enseignants"**

### 2.2 Créer un nouvel enseignant

1. Cliquez sur **"Créer"** (bouton en haut à gauche)
2. Remplissez les informations :
   - **Nom** : Nom complet de l'enseignant (obligatoire)
   - **Université/Affiliation** : Institution où il travaille
   - **Email** : Adresse email (optionnel)
   - **Google Scholar ID** : ⚠️ **IMPORTANT** - L'ID Google Scholar
     - Exemple : `kramharroubi` ou l'ID complet trouvé dans l'URL du profil
   - **Semantic Scholar Author ID** : ID alternatif (optionnel)

3. Cliquez sur **"Sauvegarder"**

### 2.3 Trouver le Google Scholar ID

Pour trouver le Google Scholar ID d'un enseignant :

1. Allez sur https://scholar.google.com/
2. Recherchez l'enseignant par son nom
3. Cliquez sur son profil
4. L'URL ressemblera à :
   - `https://scholar.google.com/citations?user=ABC123XY&hl=en`
   - Le **Google Scholar ID** est : `ABC123XY` (la partie après `user=`)

---

## 📚 Étape 3 : Importer les articles

### 3.1 Synchroniser avec Google Scholar

Une fois l'enseignant créé avec son Google Scholar ID :

1. Ouvrez la fiche de l'enseignant
2. Cliquez sur le bouton **"Synchroniser avec Google Scholar"** (en haut du formulaire)
3. Attendez quelques secondes pendant l'import
4. Un message de confirmation s'affichera avec le nombre d'articles importés

### 3.2 Vérifier les articles importés

1. Dans la fiche de l'enseignant, allez dans l'onglet **"Articles"**
2. Vous verrez tous les articles importés avec :
   - Titre
   - Année
   - Journal/Conférence
   - Nombre de citations
   - URL

### 3.3 Statistiques mises à jour

Après la synchronisation, les statistiques sont automatiquement mises à jour :
- **H-index** : Mis à jour depuis Google Scholar
- **i10-index** : Mis à jour depuis Google Scholar
- **Citations totales** : Somme des citations de tous les articles
- **Nombre d'articles** : Compté automatiquement

---

## 📊 Étape 4 : Consulter et gérer les articles

### 4.1 Voir tous les articles

1. Allez dans **Université** > **Articles**
2. Vous verrez tous les articles de tous les enseignants
3. Utilisez les filtres pour :
   - Articles récents (≥ 2020)
   - Articles cités
   - Hautes citations (> 10)

### 4.2 Trier et grouper

Dans la vue Articles, vous pouvez :
- **Trier** : Par année, citations, etc.
- **Grouper** : Par enseignant, année, journal
- **Voir en graphique** : Graphique des citations par année
- **Vue pivot** : Analyse détaillée

### 4.3 Modifier un article

1. Cliquez sur un article pour l'ouvrir
2. Vous pouvez modifier :
   - Titre
   - Année
   - Journal
   - DOI
   - URL
   - Résumé
   - Auteurs

---

## 🔄 Étape 5 : Mettre à jour les articles

### 5.1 Re-synchroniser un enseignant

Pour mettre à jour les articles d'un enseignant :

1. Ouvrez la fiche de l'enseignant
2. Cliquez à nouveau sur **"Synchroniser avec Google Scholar"**
3. Les articles existants seront mis à jour
4. Les nouveaux articles seront ajoutés

### 5.2 Détection des doublons

Le module détecte automatiquement les doublons par :
- Titre de l'article
- Enseignant associé

Les articles existants sont mis à jour au lieu d'être dupliqués.

---

## 🔍 Étape 6 : Rechercher et filtrer

### 6.1 Rechercher un enseignant

Dans la vue Enseignants :
- Utilisez la barre de recherche pour chercher par :
  - Nom
  - Affiliation
  - Google Scholar ID
- Utilisez le filtre **"Avec articles"** pour voir seulement les enseignants ayant des articles

### 6.2 Rechercher un article

Dans la vue Articles :
- Recherchez par :
  - Titre
  - Enseignant
  - Journal
  - Année
- Filtres disponibles :
  - Articles récents
  - Articles cités
  - Hautes citations

---

## 📈 Étape 7 : Analyser les données

### 7.1 Vue graphique

1. Allez dans **Université** > **Articles**
2. Cliquez sur l'icône **Graphique** (en haut à droite)
3. Visualisez les citations par année

### 7.2 Vue pivot

1. Cliquez sur l'icône **Pivot** (en haut à droite)
2. Analysez les données par :
   - Enseignant (lignes)
   - Année (colonnes)
   - Citations (mesure)

---

## ⚙️ Fonctionnalités avancées

### Bouton "Voir les articles"

Dans la fiche d'un enseignant :
- Cliquez sur **"Voir les articles"** pour voir uniquement ses articles
- Ou cliquez sur le bouton statistique **"Articles"** en haut à droite

### Vue Kanban

Dans la vue Enseignants :
- Basculez en vue **Kanban** pour voir les enseignants sous forme de cartes
- Groupez par affiliation pour une meilleure organisation

---

## ⚠️ Notes importantes

1. **Quota API** : SerpAPI a un quota gratuit limité. Surveillez votre utilisation.

2. **Google Scholar ID** : Assurez-vous d'avoir le bon ID. Si la synchronisation échoue, vérifiez l'ID.

3. **Fréquence de synchronisation** : Ne synchronisez pas trop souvent pour éviter de dépasser le quota API.

4. **Erreurs** : Si une erreur survient lors de la synchronisation :
   - Vérifiez votre clé API
   - Vérifiez le Google Scholar ID
   - Vérifiez votre connexion internet
   - Consultez les logs Odoo pour plus de détails

---

## 🎯 Exemple complet

1. **Configuration** : Ajoutez votre clé API SerpAPI dans Paramètres
2. **Création** : Créez un enseignant "Dr. John Smith" avec Google Scholar ID "ABC123XY"
3. **Synchronisation** : Cliquez sur "Synchroniser avec Google Scholar"
4. **Résultat** : 25 articles importés, H-index = 12, Citations totales = 450
5. **Consultation** : Consultez les articles dans l'onglet "Articles"
6. **Analyse** : Utilisez les vues graphique et pivot pour analyser les données

---

## 📞 Support

Si vous rencontrez des problèmes :
1. Vérifiez les logs Odoo
2. Vérifiez votre clé API SerpAPI
3. Vérifiez que le Google Scholar ID est correct
4. Assurez-vous que le module est correctement installé

