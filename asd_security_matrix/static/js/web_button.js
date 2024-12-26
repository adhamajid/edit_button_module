odoo.define('web_button', function (require) {
    'use strict';

    var core = require("web.core");
    var Sidebar = require('web.Sidebar');
    var FormView = require("web.FormView");
    var session = require("web.session");

    FormView.include({
        willStart: function () {
            var self = this;
            return this._super().then(function () {
                // Check user group
                if (self.model === 'account.move') {
                    session.user_has_group('asd_security_matrix.group_account_edit_button').then(function (hasGroup) {
                        if (!hasGroup) {
                            // Hide the Edit button if the user is not in the group
                            $('button.o_form_button_edit').hide();
                        }
                    });
                }
            });
        }
    });
});
