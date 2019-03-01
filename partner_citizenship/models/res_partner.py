# -*- coding: utf-8 -*-
# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models, api


class Citizenship(models.Model):
    _name = 'res.citizenship'


    main_citizenship_id = fields.Many2one(
        comodel_name="res.country",
        string="First Citizenship",
        help="If dual citizenship applied, this would be proposed"
             "as default"
    )
    second_citizenship_id = fields.Many2one(
        comodel_name="res.country",
        string="Second Citizenship"
    )

    @api.onchange('main_citizenship_id')
    def onchange_main_citizenship_id(self):
        """
        method to retrict remove first citiz if second are filup
        :return:
        """
        pass

    def get_partner_citizenship_id(self):
        """
        access to citizenship from method if first
        :return:
        """
        self.ensure_one()
        if self.main_citizenship_id:
            return self.main_citizenship_id.id
        else:
            return self.second_citizenship_id.id
        
class ResPartner(models.Model):

    _name = 'res.partner'
    _inherit = ['res.partner', 'res.citizenship']

