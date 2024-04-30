from odoo import models, fields

class VendorAdjustmentRequest(models.Model):
    _name = 'vendor.adjustment.request'
    _description = 'Vendor Adjustment Request'

    order_id = fields.Many2one('sale.order', string='Sales Order', required=True)
    adjustment_detail = fields.Text(string='Adjustment Detail', required=True)
    comment = fields.Text(string='Comment')