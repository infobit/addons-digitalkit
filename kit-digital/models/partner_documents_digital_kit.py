# -*- encoding: utf-8 -*-
##############################################################################
from datetime import datetime, timedelta
import time
from openerp import fields, models, api
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
import random

class partner_documents_digital_kit(models.Model):
      _name = 'partner.documents.digital.kit'
      _description = "Digital document for digital kit"

      name = fields.Char("Document")
      url_document = fields.Char("Url Document")
      type = fields.Many2one("type.document.digital.kit", "Type document")
      categ_solution_id = fields.Many2one("partner.digital.categories.solution", "Categ.Solution")
      note = fields.Text("Note")
      partner_id = fields.Many2one("res.partner", "Digital partner")

      """@api.model
      def create(self, vals_list):
        #raise Warning(vals_list)
        res = super(partner_documents_digital_kit, self).create(vals_list)
        return res"""
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
