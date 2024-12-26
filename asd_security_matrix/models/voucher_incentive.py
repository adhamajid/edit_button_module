from odoo import models, fields, api, _
from odoo.exceptions import UserError

class VoucherIncentivesInherit(models.Model):
    _inherit = 'voucher.incentive'

    has_incentives_voucher_button_use = fields.Boolean(
        string='Has Incentives Voucher Button Use',
        compute='_compute_has_incentives_voucher_button_use',
    )
    
    has_incentives_voucher_button_writeoff = fields.Boolean(
        string='Has Incentives Voucher Button Write Off',
        compute='_compute_has_incentives_voucher_button_writeoff',
    )
    
    has_incentives_voucher_button_reverse = fields.Boolean(
        string='Has Incentives Voucher Button Reverse',
        compute='_compute_has_incentives_voucher_button_reverse',
    )

    def _compute_has_incentives_voucher_button_use(self):
        for record in self:
            if self.env.user.has_group('asd_security_matrix.group_incentives_voucher_button_use'):
                record.has_incentives_voucher_button_use = True
            else:
                record.has_incentives_voucher_button_use = False 
    
    def _compute_has_incentives_voucher_button_writeoff(self):
        for record in self:
            if self.env.user.has_group('asd_security_matrix.group_incentives_voucher_button_writeoff'):
                record.has_incentives_voucher_button_writeoff = True
            else:
                record.has_incentives_voucher_button_writeoff = False 
    
    def _compute_has_incentives_voucher_button_reverse(self):
        for record in self:
            if self.env.user.has_group('asd_security_matrix.group_incentives_voucher_button_reverse'):
                record.has_incentives_voucher_button_reverse = True
            else:
                record.has_incentives_voucher_button_reverse = False 
