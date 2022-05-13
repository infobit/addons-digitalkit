# -*- encoding: utf-8 -*-
##############################################################################
from datetime import datetime, timedelta
import time
from openerp import fields, models, api
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
import random

class partner_digital_categories_solution(models.Model):
      _name = 'partner.digital.categories.solution'
      _description = "Digital categories solution for kit"

      name = fields.Many2one("digital.categories.solution", "Category solution")
      maximum_amount = fields.Float(related="name.maximum_amount", string="Maximum amount")
      amount = fields.Float("Amount")
      order_partner_id = fields.Many2one("sale.order", "Sale order Partner")
      order_kit_id = fields.Many2one("sale.order", "Sale order kit")
      date_validation_kit = fields.Date("Date validation kit")
      date_end_validation_kit = fields.Date("Date end validation kit")
      #date_order_partner_id = fields.Datetime(related="order_partner_id.date_order", string="Date of presentation Partner")
      #date_order_kit_id = fields.Datetime(related="order_kit_id.date_order", string="Date of presentation kit")
      first_amount_paid = fields.Float("First amount paid")
      second_amount_paid = fields.Float("Second amount paid")
      state = fields.Many2one("state.categ.sol.digital.kit", "State")
      date_init = fields.Date("Date init")
      date_end = fields.Date("Date end")
      note = fields.Text("Note")
      partner_id = fields.Many2one("res.partner", "Digital partner")
      documents_kit_ids = fields.One2many("partner.documents.digital.kit", "categ_solution_id", "Digital kit documents", readonly=True)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
