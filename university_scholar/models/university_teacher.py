# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import requests
import logging
from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class UniversityTeacher(models.Model):
    _name = "university.teacher"
    _description = "Enseignant"
    _rec_name = "name"

    name = fields.Char(string="Nom", required=True, index=True)
    affiliation = fields.Char(string="Université/Affiliation")
    email = fields.Char(string="Email")
    scholar_id = fields.Char(
        string="Google Scholar ID",
        help="L'ID Google Scholar de l'enseignant (ex: kramharroubi ou l'ID complet)"
    )
    semantic_scholar_id = fields.Char(
        string="Semantic Scholar Author ID",
        help="ID alternatif pour Semantic Scholar API"
    )
    total_citations = fields.Integer(
        string="Citations totales",
        compute="_compute_total_citations",
        store=False
    )
    h_index = fields.Integer(string="H-index", readonly=True)
    i10_index = fields.Integer(string="i10-index", readonly=True)
    article_ids = fields.One2many(
        "university.article",
        "teacher_id",
        string="Articles"
    )
    article_count = fields.Integer(
        string="Nombre d'articles",
        compute="_compute_article_count",
        store=False
    )

    @api.depends('article_ids')
    def _compute_article_count(self):
        for teacher in self:
            teacher.article_count = len(teacher.article_ids)

    @api.depends('article_ids.citations')
    def _compute_total_citations(self):
        for teacher in self:
            teacher.total_citations = sum(teacher.article_ids.mapped('citations'))

    def action_fetch_articles(self):
        """Importe les articles depuis Google Scholar via SerpAPI"""
        self.ensure_one()
        
        if not self.scholar_id:
            raise exceptions.UserError(_(
                "Veuillez d'abord renseigner le Google Scholar ID pour %s" % self.name
            ))

        # Récupération de la clé API depuis les paramètres système
        api_key = self.env['ir.config_parameter'].sudo().get_param('university_scholar.serpapi_key')
        
        if not api_key:
            raise exceptions.UserError(_(
                "Clé API SerpAPI non configurée. "
                "Veuillez configurer 'university_scholar.serpapi_key' dans les paramètres système."
            ))

        try:
            # Appel à l'API SerpAPI pour Google Scholar Author
            url = "https://serpapi.com/search.json"
            params = {
                "engine": "google_scholar_author",
                "author_id": self.scholar_id,
                "api_key": api_key,
                "hl": "fr",  # Langue: français
            }

            _logger.info("Fetching articles for teacher %s (Scholar ID: %s)", self.name, self.scholar_id)
            response = requests.get(url, params=params, timeout=30)
            
            if response.status_code != 200:
                error_msg = f"Erreur API SerpAPI: {response.status_code} - {response.text}"
                _logger.error(error_msg)
                raise exceptions.UserError(_(error_msg))

            data = response.json()
            
            # Mise à jour des statistiques de l'auteur si disponibles
            author_info = data.get("author", {})
            if author_info:
                self.h_index = author_info.get("h_index", {}).get("value", 0) or 0
                self.i10_index = author_info.get("i10_index", {}).get("value", 0) or 0
                if not self.affiliation and author_info.get("affiliations"):
                    self.affiliation = author_info.get("affiliations", [""])[0]

            # Traitement des articles
            articles = data.get("articles", [])
            created_count = 0
            updated_count = 0

            for article_data in articles:
                # Extraction des données de l'article
                title = article_data.get("title", "")
                if not title:
                    continue

                # Gestion des citations
                cited_by = article_data.get("cited_by", {})
                citations = 0
                if isinstance(cited_by, dict):
                    citations = cited_by.get("value", 0) or 0
                elif isinstance(cited_by, (int, str)):
                    try:
                        citations = int(cited_by)
                    except (ValueError, TypeError):
                        citations = 0

                # Extraction de l'année
                year = article_data.get("year")
                if year:
                    try:
                        year = int(year)
                    except (ValueError, TypeError):
                        year = None
                else:
                    year = None

                # Extraction des autres métadonnées
                journal = article_data.get("publication", "")
                article_url = article_data.get("link", "")
                authors = article_data.get("authors", [])
                authors_str = ", ".join([a.get("name", "") for a in authors if isinstance(a, dict) and a.get("name")])

                # Préparation des valeurs pour création/mise à jour
                vals = {
                    "name": title,
                    "year": year,
                    "journal": journal or "",
                    "url": article_url,
                    "citations": citations,
                    "teacher_id": self.id,
                    "authors": authors_str,
                }

                # Vérification des doublons par titre et enseignant
                existing = self.env["university.article"].search([
                    ("name", "=", title),
                    ("teacher_id", "=", self.id)
                ], limit=1)

                if existing:
                    # Mise à jour de l'article existant
                    existing.write(vals)
                    updated_count += 1
                else:
                    # Création d'un nouvel article
                    self.env["university.article"].create(vals)
                    created_count += 1

            message = _(
                "Import terminé: %d articles créés, %d articles mis à jour."
            ) % (created_count, updated_count)
            
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('Succès'),
                    'message': message,
                    'type': 'success',
                    'sticky': False,
                }
            }

        except requests.exceptions.RequestException as e:
            error_msg = f"Erreur de connexion à l'API: {str(e)}"
            _logger.error(error_msg)
            raise exceptions.UserError(_(error_msg))
        except Exception as e:
            error_msg = f"Erreur lors de l'import: {str(e)}"
            _logger.error(error_msg, exc_info=True)
            raise exceptions.UserError(_(error_msg))

    def action_view_articles(self):
        """Action pour voir tous les articles de l'enseignant"""
        self.ensure_one()
        return {
            'name': _('Articles de %s') % self.name,
            'type': 'ir.actions.act_window',
            'res_model': 'university.article',
            'view_mode': 'list,form',
            'domain': [('teacher_id', '=', self.id)],
            'context': {'default_teacher_id': self.id},
        }

