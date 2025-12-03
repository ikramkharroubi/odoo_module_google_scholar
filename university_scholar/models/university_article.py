# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class UniversityArticle(models.Model):
    _name = "university.article"
    _description = "Article scientifique"
    _rec_name = "name"
    _order = "year desc, citations desc"

    name = fields.Char(string="Titre", required=True, index=True)
    year = fields.Integer(string="Année", index=True)
    journal = fields.Char(string="Journal/Conférence")
    doi = fields.Char(string="DOI", index=True)
    url = fields.Char(string="URL")
    citations = fields.Integer(string="Citations", default=0, index=True)
    authors = fields.Char(string="Auteurs")
    abstract = fields.Text(string="Résumé")
    teacher_id = fields.Many2one(
        "university.teacher",
        string="Enseignant",
        required=True,
        ondelete="cascade",
        index=True
    )
    teacher_name = fields.Char(
        related="teacher_id.name",
        string="Nom de l'enseignant",
        store=True,
        readonly=True
    )

