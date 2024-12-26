from odoo import models, fields, api, _
from odoo.exceptions import UserError
import xml.etree as etr
import xml.etree.ElementTree as ET
from ast import literal_eval
import logging


_logger = logging.getLogger(__name__)

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    edit_hide_css = fields.Html(
        string='CSS for hiding Edit button', 
        sanitize=False, 
        compute='_compute_edit_hide_css'
    )

    lock_order_line_css = fields.Html(
        string='CSS for locking order_line field', 
        sanitize=False, 
        compute='_compute_lock_order_line_css'
    )


    def _compute_edit_hide_css(self):
    # Memeriksa apakah pengguna termasuk dalam grup yang memiliki hak untuk menyembunyikan tombol edit
        user_has_edit_hide_css_group = self.env.user.has_group('asd_security_matrix.group_account_edit_button')

        for order in self:
            # Jika pengguna berada dalam grup tertentu, sembunyikan tombol edit
            if user_has_edit_hide_css_group:
                order.edit_hide_css = '<style>.o_form_button_edit {display: none !important;}</style>'
            else:
                order.edit_hide_css = False

    @api.depends('type')
    def _compute_lock_order_line_css(self):
        for order in self:
            if order.type in ['out_invoice', 'in_invoice'] :
                order.lock_order_line_css = False
            else:
                order.lock_order_line_css = '<style>.o_field_x2many_list_row_add {display: none !important;} .o_list_record_remove {display: none !important;}</style>'


    has_reset_draft = fields.Boolean(
        string='Has Reset To Draft ',
        compute='_compute_has_reset_draft',
    )
    
    has_register_payment = fields.Boolean(
        string='Has Register Payment ',
        compute='_compute_has_register_payment',
        store=False
    )

    has_write_off_acc = fields.Boolean(
        string='Has Write Off ',
        compute='_compute_has_write_off_acc',
    )    
    
        

    # Define the compute has_reset_draft
    def _compute_has_reset_draft(self):
    # Memeriksa grup yang dimiliki oleh pengguna
        user_has_reset_draft_group = self.env.user.has_group('asd_security_matrix.group_account_invoice_reset_draft')
        user_has_bills_reset_draft_group = self.env.user.has_group('asd_security_matrix.group_account_bills_reset_draft')

        for record in self:
            # Cek jika tipe invoice adalah 'out_invoice'
            if record.type == 'out_invoice':
                record.has_reset_draft = user_has_reset_draft_group
            # Cek jika tipe invoice adalah 'in_invoice'
            elif record.type == 'in_invoice':
                record.has_reset_draft = user_has_bills_reset_draft_group
            else:
                # Set False untuk tipe lain selain 'out_invoice' dan 'in_invoice'
                record.has_reset_draft = False
 

    # Define the compute has_register_payment
    def _compute_has_register_payment(self):
        for record in self:
            if record.type == 'out_invoice':
                record.has_register_payment = (
                    self.env.user.has_group('asd_security_matrix.group_invoice_register_payment')
                )
            elif record.type == 'in_invoice':
                record.has_register_payment = (
                    self.env.user.has_group('asd_security_matrix.group_bills_register_payment')
                )
            elif record.type == 'in_refund':
                record.has_register_payment = (
                    self.env.user.has_group('asd_security_matrix.group_refund_register_payment')
                )
            elif record.type == 'out_refund':
                record.has_register_payment = (
                    self.env.user.has_group('asd_security_matrix.group_credit_notes_register_payment')
                )
            else:
                record.has_register_payment = True

    def _compute_has_write_off_acc(self):
        for record in self:
            if record.type == "out_invoice" :
                record.has_write_off_acc = (
                    self.env.user.has_group('asd_security_matrix.group_account_invoice_writeoff')
                )
            else:
                record.has_write_off_acc = True
                