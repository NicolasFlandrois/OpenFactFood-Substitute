#!usr/bin/python3.7
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST
# Author: Nicolas Flandrois

import os 
import platform
from models import Product, Category
from view import View

def clean():
    """This function will clear the terminal's screen. The command is 
    automaticaly detected according to the system OS you run it."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear") #This command will work on Linux and OSx systems.

def main():
    """Main running function."""
    category_id = View.categories_list()
    prod_id = View.products_list(category_id)
    View.product_sheet(prod_id)
    print("(Appuyez sur Entrer pour continuer)")
    input()
    clean()
    View.prod_sub(prod_id)
    print("(Appuyez sur Entrer pour continuer)")
    input()
    clean()
    View.sub_tbl()


if __name__ == '__main__':
    main()
