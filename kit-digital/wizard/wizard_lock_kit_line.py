# -*- encoding: utf-8 -*-
##############################################################################
from openerp import models, fields, api
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from datetime import datetime
from openerp.osv import osv

class wizard_lock_kit_line(models.TransientModel):
    _name = "wizard.lock.kit.line"

    @api.multi
    def lock(self, data):
        for i in self.env['kit.line'].browse(data['active_ids']): 
            i.write({'lock': True})
        return True
wizard_lock_kit_line()
