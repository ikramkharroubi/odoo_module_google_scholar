# University Scholar - Module Odoo 18

Module Odoo pour gérer les enseignants et leurs articles Google Scholar via l'API SerpAPI.

## Fonctionnalités

- Gestion des enseignants avec Google Scholar ID
- Import automatique des articles depuis Google Scholar (via SerpAPI)
- Affichage des citations, h-index, i10-index
- Vues Kanban, Liste, Graphique et Pivot

## Installation

1. Copiez le module dans votre dossier `addons`:
   ```bash
   cp -r university_scholar /path/to/odoo/addons/
   ```

2. Redémarrez Odoo

3. Activez le mode développeur

4. Allez dans Apps → Mettre à jour la liste des applications

5. Recherchez "University Scholar" et installez-le

## Configuration

1. Allez dans Paramètres → Technique → Paramètres → University Scholar
2. Entrez votre clé API SerpAPI
3. Obtenez votre clé sur: https://serpapi.com/

## Utilisation

1. Créez un enseignant avec son Google Scholar ID
2. Cliquez sur "Synchroniser les articles" pour importer les articles
3. Consultez les statistiques (citations, h-index, etc.)

## Auteur

Ikram Kharroubi - ikramkharou@gmail.com

## Licence

LGPL-3

## Modules MuK Backend Theme

Ce repository inclut également les modules MuK Backend Theme pour Odoo 18:
- `muk_web_chatter` - Amélioration du chatter
- `muk_web_dialog` - Dialogues améliorés
- `muk_web_appsbar` - Barre d'applications
- `muk_web_colors` - Gestion des couleurs
- `muk_web_theme` - Thème backend principal

### Installation des modules MuK

1. Installez les modules dans cet ordre:
   - `muk_web_chatter`
   - `muk_web_dialog`
   - `muk_web_appsbar`
   - `muk_web_colors`
   - `muk_web_theme` (en dernier)

2. Redémarrez Odoo après chaque installation

3. Activez le thème dans Paramètres → Général → Interface
