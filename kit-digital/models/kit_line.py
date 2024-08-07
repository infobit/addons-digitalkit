# -*- coding: utf-8 -*-
from openerp import api, fields, models
from openerp import tools
from random import randint
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
from odoo import SUPERUSER_ID
from dateutil import tz
import re
from openerp.exceptions import UserError

import logging

_logger = logging.getLogger(__name__)


class KitLine(models.Model):

    _name = "kit.line"
    _description = "Kit Line"
    _order = "create_date desc"

    name = fields.Char(string="Asunto")
    description = fields.Text(string="Descripción")
    user_id = fields.Many2one('res.users', "Empleado", default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string="Cliente")
    working_hours = fields.Float(string="Horas trabajadas")
    invoice_hours = fields.Float(string="Invoice hours")
    date = fields.Date(string="Fecha", default=fields.Date.today())
    product_id = fields.Many2one('product.product', string="Producto")
    qty_invoice = fields.Float(string="Cant.facturación")
    price = fields.Float(string="Precio")
    amount = fields.Float(string="Importe", compute='amount_calculated')
    lock = fields.Boolean(string="Liquidado")
    discount = fields.Float(string="%Dto")
    internal = fields.Boolean(string="Interno")

    @api.model
    def create(self,values):
        rec = super(KitLine, self).create(values)
        if rec.working_hours != 0.0:
           rec.qty_invoice = rec.working_hours
        #if rec.product_id and rec.partner_id:
        #   rec.onchange_partner_product_id()
        return rec

    @api.multi
    def unlink(self):
        for rec in self:
            if rec.lock:
                raise UserError('No puedes borrar la línea, esta liquidada!')
        return super(KitLine, self).unlink()

    @api.multi
    def amount_calculated(self):
        for rec in self:
            rec.amount = rec.price * rec.qty_invoice

    @api.multi
    @api.onchange('partner_id', 'product_id')
    def onchange_partner_product_id(self):
          for rec in self:
              if not rec.lock:
                 if rec.product_id and rec.partner_id:
                    if rec.product_id and rec.partner_id.property_product_pricelist and rec.partner_id.property_product_pricelist.id != 1:
                       #buscar si tiene tarifa el cliente para ese producto
                       rec.price = rec.product_id.lst_price
                       for item in rec.partner_id.property_product_pricelist.item_ids:
                           if item.applied_on == '1_product' and item.product_tmpl_id.id == rec.product_id.product_tmpl_id.id:
                              if item.compute_price == 'fixed':
                                 #raise Warning(item.fixed_price)
                                 rec.price = item.fixed_price
                              else:
                               if item.compute_price == 'percentage':
                                 rec.price = rec.product_id.lst_price - ((rec.product_id.lst_price * item.percent_price) / 100)
                                 rec.discount = item.percent_price
                               else:
                                if item.compute_price == 'fixedpercentage':
                                 rec.price = item.fixed_price - ((item.fixed_price * item.percent_price) / 100)
                                 rec.discount = item.percent_price
                                else:
                                 rec.price = rec.product_id.lst_price
