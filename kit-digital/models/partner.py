# -*- encoding: utf-8 -*-
##############################################################################
from datetime import datetime, timedelta
import time
from openerp import fields, models, api
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp

class partner(models.Model):
    _inherit = 'res.partner'

    grant_awarded = fields.Char('Grand Awarded')
    categ_kit_ids = fields.One2many('partner.digital.categories.solution', 'partner_id', 'Categories of digital solutions')
    documents_kit_ids = fields.One2many('partner.documents.digital.kit', 'partner_id', 'Digital kit documents')
    beneficiary_segment = fields.Many2one('beneficiary.segments', 'Segment - Bonus amount')
    state_kit = fields.Selection([('pendiente', '[Paso 1] Pendiente de solicitar kit'), ('solicitado', '[Paso 2] Kit Solicitado'), ('aceptado', '[Paso 3] Kit Aceptado'), ('en_curso', '[Paso 4] Trabajos iniciados'), ('finalizado', '[Paso 5] Trabajos Finalizados'), ('renunciado', '[Paso 6] Renunciado'), ('denegado', '[Paso 7] Denegado')], string="Estado")
    acept_date = fields.Date("Fecha Aceptación")
    date_end = fields.Date("Fecha Fin")
    internal_note_kit = fields.Text("Notas internas")
    kit_lines = fields.One2many('kit.line', 'partner_id', 'Lineas kit - Trabajos')
    code_bono = fields.Char("Codigo Bono-Cobro")

    @api.onchange("acept_date")
    def calc_date_end(self):
        for s in self:
            if s.acept_date:
               #raise Warning(timedelta(days=180))
               s.date_end = datetime.strptime(s.acept_date,'%Y-%m-%d') + timedelta(days=180)
