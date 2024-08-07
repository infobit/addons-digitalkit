# -*- encoding: utf-8 -*-
##############################################################################
from datetime import datetime, timedelta
import time
from openerp import fields, models, api
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
import random

class digital_categories_solution(models.Model):
      _name = 'digital.categories.solution'
      _description = "Digital categories solution"

      name = fields.Char("Category solution")
      maximum_amount = fields.Float("Maximum amount")
      note = fields.Text("Note")
      first_percentaje = fields.Float('%First amount')
      second_percentaje = fields.Float('%Second amount')
      
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
