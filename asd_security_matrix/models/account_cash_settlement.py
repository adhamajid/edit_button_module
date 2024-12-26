from odoo import models, fields, api, _
from odoo.exceptions import UserError

class CashSettlementInherit(models.Model):
    _inherit = 'account.cash.settlement'

    has_register_payment_n_return_advance_settlement = fields.Boolean(
        string='Has Register Payment and Return Advance',
        compute='_compute_has_register_payment_n_return_ad',
    )
    

    def _compute_has_register_payment_n_return_ad(self):
        for record in self:
            if self.env.user.has_group('asd_security_matrix.group_cashadv_settlement_payment_n_return'):
                record.has_register_payment_n_return_advance_settlement = True
            else:
                record.has_register_payment_n_return_advance_settlement = False 
