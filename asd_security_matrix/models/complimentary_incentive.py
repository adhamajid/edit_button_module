from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ComplimentaryInherit(models.Model):
    _inherit = 'complimentary'

    has_reverse_complimentary = fields.Boolean(
        string='Has Reverse In Complimentary',
        compute='_compute_has_reverse_complimentary',
    )

    has_resettled_ar_complimentary = fields.Boolean(
        string='Has Resettled Ar In Complimentary',
        compute='_compute_has_resettled_ar_complimentary',
    )

    has_cancel_complimentary = fields.Boolean(
        string='Has Cancel In Complimentary',
        compute='_compute_has_cancel_complimentary',
    )

    has_refund_complimentary = fields.Boolean(
        string='Has Refund In Complimentary',
        compute='_compute_has_refund_complimentary',
    )

    has_set_to_draft_complimentary = fields.Boolean(
        string='Has Set To Draft In Complimentary',
        compute='_compute_has_set_to_draft_complimentary',
    )
    

    def _compute_has_reverse_complimentary(self):
        for record in self:
            if self.env.user.has_group('asd_security_matrix.group_incentives_complimentary_button_reverse'):
                record.has_reverse_complimentary = True
            else:
                record.has_reverse_complimentary = False 

    def _compute_has_resettled_ar_complimentary(self):
        for record in self:
            if self.env.user.has_group('asd_security_matrix.group_incentives_complimentary_button_resettled_ar'):
                record.has_resettled_ar_complimentary = True
            else:
                record.has_resettled_ar_complimentary = False 

    def _compute_has_cancel_complimentary(self):
        for record in self:
            if self.env.user.has_group('asd_security_matrix.group_incentives_complimentary_button_cancel'):
                record.has_cancel_complimentary = True
            else:
                record.has_cancel_complimentary = False 

    def _compute_has_refund_complimentary(self):
        for record in self:
            if self.env.user.has_group('asd_security_matrix.group_incentives_complimentary_button_refund'):
                record.has_refund_complimentary = True
            else:
                record.has_refund_complimentary = False 

    def _compute_has_set_to_draft_complimentary(self):
        for record in self:
            if self.env.user.has_group('asd_security_matrix.group_incentives_complimentary_button_set_to_draft'):
                record.has_set_to_draft_complimentary = True
            else:
                record.has_set_to_draft_complimentary = False 
