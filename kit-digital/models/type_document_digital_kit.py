# -*- encoding: utf-8 -*-
##############################################################################
from datetime import datetime, timedelta
import time
from openerp import fields, models, api
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
import random

class type_document_digital_kit(models.Model):
      _name = 'type.document.digital.kit'
      _description = "Digital documents of digital kit"

      name = fields.Char("Type document")
      note = fields.Text("Note")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
