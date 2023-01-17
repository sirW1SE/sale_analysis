# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrderAnalysis(models.Model):
    _inherit = 'sale.order.line'

    sale_order_image = fields.Binary(string="Image",
                                     related="product_id.image_1920")