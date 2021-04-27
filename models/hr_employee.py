# Copyright (C) 2018 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models
from  odoo.exceptions import  UserError



class AccountIdea(models.Model):
    _inherit = "res.partner"
    
    state = fields.Selection([
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('approved', 'Approved'),
            ],default='draft')

    def draft_progressbar(self):
      self.write({'state': 'draft',})

    def confirmed_progressbar(self):
      self.write({'state': 'confirmed'})
 
#This function is triggered when the user clicks on the button 'In progress'

    def approved_progressbar(self):
      self.write({'state': 'approved'})