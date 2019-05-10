#!usr/bin/python3
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

from menu import Menu


if __name__ == '__main__':
	cycle0 = Menu()
	cycle0.question(cycle0.q[0], cycle0.c0)

#Stocker les choix Noisette/jam/coulis dans menu C1A C1B C1C en tuple
	if cycle0.c == "1":
		c1 = ["Noisette Cacao", "Speculos", "Beurre de Cacahuète"]
	elif cycle0.c == "2":
		c1 = ["Confiture de Fraise", "Confiture d'Abricot", "Confiture d'Orange"]
	else:
		c1 = ["Coulis de Fraise", "Miel", "Sirop d'érable"]

	cycle1 = Menu()
	cycle1.question(cycle1.q[1], c1)

	cycle2 = Menu()
	cycle2.question(cycle2.q[2], cycle2.c2)

	cycle3 = Menu()
	cycle3.question(cycle3.q[3], cycle3.c3)