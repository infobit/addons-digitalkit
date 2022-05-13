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
		'base'
	], 
	"category" : "Partner Modules",
	"init_xml" : [],
	"demo_xml" : [],
	"data" : [
                'views/state_categ_sol_digital_kit.xml',
                'views/type_document_digital_kit.xml',
                'views/beneficiary_segments.xml',
                'views/digital_categories_solution.xml',
                'views/partner_digital_categories_solution.xml',
                'views/partner_documents_digital_kit.xml',
                'views/partner.xml',
                'data/category_solutions.xml',
                'data/segments.xml',
	],
	"installable": True
}
