from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountPaymentInherit(models.Model):
    _inherit = 'account.payment'

    has_reverse_acc = fields.Boolean(
        string='Has Reverse Off ',
        compute='_compute_has_reverse_acc',
    )

    def _compute_has_reverse_acc(self):
        for record in self:
            if self.env.user.has_group('asd_security_matrix.group_account_vendor_reserve'):
                record.has_reverse_acc = True
            else:
                record.has_reverse_acc = False