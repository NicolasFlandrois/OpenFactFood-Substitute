#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

class View(object):
	"""docstring for View"""
	def __init__(self, arg):
		super(View, self).__init__()
		self.arg = arg

# class View
# établire en methode statique (Statelass static avec parametre (pas de variables)) les fonction:
# • category (e.g. view.category(category) > self.category(param))
# • view produit par catégories
# • view 1 produit spécifique
#    ◇ Fiche produit
# • view 1 produit et son substitut
# • view menu
#    ◇ reprendre ce qui a été fait dans fichier menu
#    ◇ faire 1 view par menu
#    ◇ vue bloquante > attends une réponce
#       ▪ affichage
#       ▪ input
#       ▪ output
#    ◇ stateless
#       ▪ static
#       ▪ param
#       ▪ (pas de variables en param)
# Translate ALL in english!