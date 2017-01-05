# -*- coding: utf-8 -*-
from openerp import models, fields

class Ingredient (models.Model):
	_name = 'recipe.Ingredient'
	name = fields.Char('Title', required=True)
	date_release = fields.Date('Release Date')
	author_ids = fields.Many2many('res.partner', string='Authors')
	
# Name (enforce naming convention)
#		Image
#		Description
#		Purchase Unit
#		Usage unit
#		Yield %
#		Categories
#		Used In
