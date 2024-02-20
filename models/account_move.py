import_file


from odoo import fields, models, api, _
from odoo.exceptions import UserError
import base64

class AM(models.Model):
    _inherit = 'account.move'
    def _check_balanced(self):
        if self.context.get('import_file',False):
            self = self.with_context(check_move_validity=False)
        return super()._check_balanced()