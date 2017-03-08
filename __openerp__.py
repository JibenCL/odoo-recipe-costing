# -*- coding: utf-8 -*-
{
	'name': 'Recipe Costing',
	
	'summary': "Recipe Management & Costing Module",
	
	# Description: Multiline, plain text or RST (http://docutils.sourceforge.net/docs/user/rst/quickstart.html)
	'description': """  """,
	
	'author': "Jon Tillman",
	
	'license': "AGPL-3"
    
	'website': "",
	
	# Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml for the full list
    'category': 'Specific Industry Applications',
	'category': 'Inventory',
    'version': '0.1',
	
	# any module necessary for this one to work correctly
    'depends': ['base'],
	
	# always loaded
    'data': [
        'security/ir.model.access.csv',
    ],
	
	# only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
	
	'installable': 'true'
}

# Ingredients Model
{
	'name': "Ingredients",
	'summary': "Ingredient Management",
	'depends': ['base'],
	'data': ['views/ingredient.xml',],
}

# Recipe Model
{
	'name': "Recipe",
	'summary': "Recipe Management & Costing",
	'depends': ['base'],
	'data': ['views/recipe.xml',],
}

# Categories Model
{
	'name': "Categories",
	'summary': "Category Management",
	'depends': ['base'],
	'data': ['views/category.xml',],
}
