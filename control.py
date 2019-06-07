#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

from models import Product, Category
from view import View

def main():
	"""docstring ici"""
	category_id = View.categories_list()
	prod_id = View.products_list(category_id)
	View.product_sheet(prod_id)
	View.prod_sub(prod_id)


if __name__ == '__main__':
	main()