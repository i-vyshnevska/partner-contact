# -*- coding: utf-8 -*-
# Copyright 2019 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "Contact citizenship",
    "summary": "Add citizenship field to contacts",
    "version": "10.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "https://odoo-community.org/",
    "author": "CamptoCamp, Odoo Community Association (OCA)",
    "contributors": [
    ],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "auto_install": False,
    "depends": [
        "base",
    ],
    "data": [
        "views/res_partner.xml",
        "security/ir.model.access.csv",
    ],
}
