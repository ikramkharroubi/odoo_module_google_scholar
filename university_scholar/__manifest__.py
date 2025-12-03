# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'University Scholar',
    'version': '1.0',
    'author': 'Ikram',
    'category': 'Education',
    'summary': 'Gestion des enseignants et leurs articles Google Scholar',
    'description': """
        Module pour gérer les enseignants et leurs publications scientifiques
        via l'API Google Scholar (SerpAPI).
        
        Fonctionnalités:
        - Gestion des enseignants avec Google Scholar ID
        - Import automatique des articles depuis Google Scholar
        - Affichage des citations et métadonnées des articles
    """,
    'depends': ['base', 'base_setup'],
    'data': [
        'security/ir.model.access.csv',
        'views/university_teacher_views.xml',
        'views/university_article_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'external_dependencies': {
        'python': ['requests'],
    },
}

