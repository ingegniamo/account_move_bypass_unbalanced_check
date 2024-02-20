

from odoo import fields, models, api, _
from odoo.exceptions import UserError
import base64

class AM(models.Model):
    _inherit = 'account.move'
    def _check_balanced(self):
        if not self.env.context.get('import_file',False):
           
            return super()._check_balanced()