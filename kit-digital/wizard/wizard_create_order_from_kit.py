# -*- encoding: utf-8 -*-
from openerp import models, fields, api
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from datetime import datetime
from openerp.osv import osv


class wizard_create_order_from_kit(models.TransientModel):
    _name = "wizard.create.order.from.kit"
    _description = "Create order"

    @api.multi
    def create_order(self, data):
        #check partners

        lista = self.env['kit.line'].browse(data['active_ids'])
        if all(elemento.partner_id != lista[0].partner_id for elemento in lista):
           raise Warning("Las lineas seleccionadas tiene que pertenecer al mismo cliente")

        if lista[0].partner_id:
            cli = lista[0].partner_id
            nameseq = self.env['ir.sequence'].get('sale.order')
            payment = False
            if cli.property_payment_term_id:
                payment = cli.property_payment_term_id.id
            fiscal = False 
            if cli.property_account_position_id:
                fiscal = cli.property_account_position_id.id
            modepayment = False
            if cli.customer_payment_mode_id:
                modepayment = cli.customer_payment_mode_id.id
            pedido  = self.env['sale.order'].create({
                'ib_parteaveria': True,
                'name': nameseq, 
                'partner_id': cli.id, 
                'pricelist_id': cli.property_product_pricelist.id, 
                'payment_mode_id': modepayment, 
                'payment_term_id': payment, 
                'fiscal_position_id': fiscal, 
                'user_id':  self._uid,
                'origin':"Kit Digital"
                })
            if pedido:
                for linep in lista:
                    if linep.product_id:
                        self.env['sale.order.line'].create({
                                'product_id': linep.product_id.id, 
                                'order_id': pedido.id, 
                                'discount': linep.discount, 
                                'product_uos_qty': linep.qty_invoice, 
                                'product_uom_qty': linep.qty_invoice, 
                                'tax_id': [(6, 0, [x.id for x in linep.ib_product_id.taxes_id])]})


                                
        else:
            raise Warning("No ha indicado cliente en la tarea")
        return True

wizard_create_order_from_kit()