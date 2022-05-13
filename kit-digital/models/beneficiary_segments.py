# -*- encoding: utf-8 -*-
##############################################################################
from datetime import datetime, timedelta
import time
from openerp import fields, models, api
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
import random

class beneficiary_segments(models.Model):
      _name = 'beneficiary.segments'
      _description = "Beneficiary segments"

      name = fields.Char("Bonus amount")
      segment = fields.Char("Segment")
      note = fields.Text("Note")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
