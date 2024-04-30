from odoo import models, fields

class VendorAdjustmentRequestWizard(models.TransientModel):
    _name = 'vendor.adjustment.request.wizard'
    _description = 'Vendor Adjustment Request Wizard'

    order_id = fields.Many2one('sale.order', string='Sales Order', required=True)
    adjustment_detail = fields.Text(string='Adjustment Detail', required=True)
    comment = fields.Text(string='Comment')

    def submit_adjustment_request(self):
        self.env['vendor.adjustment.request'].create({
            'order_id': self.order_id.id,
            'adjustment_detail': self.adjustment_detail,
            'comment': self.comment,
        })
        return {'type': 'ir.actions.act_window_close'}