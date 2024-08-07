# -*- encoding: utf-8 -*-
##############################################################################
from datetime import datetime, timedelta
import time
from openerp import fields, models, api
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
import random

class state_categ_sol_digital_kit(models.Model):
      _name = 'state.categ.sol.digital.kit'
      _description = "State Digital category solutions"
      name = fields.Char("State")
      note = fields.Text("Note")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
