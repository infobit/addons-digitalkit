# encoding: utf-8
{
	"name" : "Management of the digital kit in partners",
	"version" : "11.0",
	"description" : """
Management of the digital kit in partners
Developed for Infobit informática s.l.
        """,
	"author" : "Infobit Informática",
	"website" : "http://www.infobit.es",
	"depends" : [ 
		'base', 'account', 'sale'
	], 
	"category" : "Partner Modules",
	"init_xml" : [],
	"demo_xml" : [],
	"data" : [
                'security/kit_security.xml',
                'security/ir.model.access.csv',
                'views/state_categ_sol_digital_kit.xml',
                'views/type_document_digital_kit.xml',
                'views/beneficiary_segments.xml',
                'views/digital_categories_solution.xml',
                'views/partner_digital_categories_solution.xml',
                'views/partner_documents_digital_kit.xml',
                'views/partner.xml',
                'wizard/wizard_create_order_from_kit.xml',
                'views/kit_line.xml',
                'views/invoice.xml',
                'wizard/wizard_lock_kit_line.xml',
                'data/category_solutions.xml',
                'data/segments.xml',
                'report/report_kit_line.xml',
                'report/report_kit_line_internal.xml',
                'report/report_kit_line_withoutamount.xml',
                'report/reports.xml'
	],
	"installable": True
}
