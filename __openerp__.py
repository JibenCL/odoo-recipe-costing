{

'name': 'Base',

'version': '1.3',

'category': 'Hidden',

'description': """

The kernel of OpenERP, needed for all installation.

===================================================

""",

'author': 'OpenERP SA',

'maintainer': 'OpenERP SA',

'website': 'http://www.openerp.com',

'depends': [],

'data': [

'base_data.xml',

'res/res_currency_data.xml',

'res/res_country_data.xml',

'security/base_security.xml',

'module/module_report.xml',

'module/wizard/base_module_update_view.xml',

'res/res_company_view.xml',

'res/res_security.xml',

'security/ir.model.access.csv',

],

'demo': [

'base_demo.xml',

'res/res_partner_demo.xml',

'res/res_partner_demo.yml',

'res/res_partner_image_demo.xml',

],

'test': [

'tests/base_test.yml',

'tests/test_osv_expression.yml',

'tests/test_ir_rule.yml', # <-- These tests modify/add/delete ir_rules.

],

'installable': True,

'auto_install': True,

}