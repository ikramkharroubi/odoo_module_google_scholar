# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    serpapi_key = fields.Char(
        string="SerpAPI Key",
        config_parameter='university_scholar.serpapi_key',
        help="Clé API SerpAPI pour accéder à Google Scholar. "
             "Obtenez votre clé sur https://serpapi.com/"
    )

