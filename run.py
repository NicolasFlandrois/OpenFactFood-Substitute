#!usr/bin/python3
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

from menu import Menu

c = None
#Category menu's questions & choices
q0 = "Veuillez choisir une catégorie: "
c0 = ['pâte à tartiner', 'confiture', 'liquide']
#Products's questions & choices
q1 = "veuillez choisir un produit : "
c1 = [] #This list will be define later depending on previous answer
#Sustitution's questions & choices
q2 = "Voulez vous substituer ce produit? "
c2 = ["Oui", "Non"]
#Substitutes Historic's questions & choices
q3 = "Historique de substitution? "
c3 = ["Oui", "Non"]

#TESTS LINES
quest0 = Menu(q0, c0)
quest0.menu(q0, c0)

if quest0.c == "1":
	c1 = ["Noisette Cacao", "Speculos", "Beurre de Cacahuète"]
elif quest0.c == "2":
	c1 = ["Confiture de Fraise", "Confiture d'Abricot", "Confiture d'Orange"]
else:
	c1 = ["Coulis de Fraise", "Miel", "Sirop d'érable"]
quest1 = Menu(q1, c1)
quest1.menu(q1, c1)

quest2 = Menu(q2, c2)
quest2.menu(q2, c2)

quest3 = Menu(q3, c3)
quest3.menu(q3, c3)