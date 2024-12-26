from odoo import models, fields, api, _
from odoo.exceptions import UserError

class CashAdvanceInherit(models.Model):
    _inherit = 'account.cash.advance',

    has_register_payment_cash_advance_preapproval = fields.Boolean(
        string='Has Register Payment Cash Advance Pre-Approval',
        compute='_compute_has_register_payment_cash_advance_pre',
    )

    def _compute_has_register_payment_cash_advance_pre(self):
        for record in self:
            if self.env.user.has_group('asd_security_matrix.group_cashadv_register_payment'):
                record.has_register_payment_cash_advance_preapproval = True
            else:
                record.has_register_payment_cash_advance_preapproval = False