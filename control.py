#!usr/bin/python3.7
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST
# Author: Nicolas Flandrois

import os 
import platform
from sys import exit
from models import Product, Category
from view import View

def clean():
    """This function will clear the terminal's screen. The command is 
    automaticaly detected according to the system OS you run it."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear") #This command will work on Linux and OSx systems.

def return_or_quit(responce):
    """This function will either Quit the programm, or Return to main menu."""
    if responce == 'r':
        pass
    elif responce == 'q':
        exit()
    else:
        continue

def main():
    """Main running function."""
    print("Bienvenu dans ce programme.")
    while True:
        responce = View.main_menu()
        clean()
        if responce in ["r", "q"]:
            return_or_quit(responce)
        elif responce == 1:
            category_id = View.categories_list()
            return_or_quit(category_id)
            prod_id = View.products_list(category_id)
            return_or_quit(prod_id)
            clean()
            
            View.product_sheet(prod_id)
            nextmove = input("(Appuyez sur Entrer pour continuer)")
            return_or_quit(nextmove)
            clean()
            
            choice = View.sub_menu()
            return_or_quit(choice)
            clean()
            
            if choice == 1:
                View.prod_sub(prod_id)
                # No return_or_quit The choice Not to substitute 
                # needs to be deliberate
                clean()
            else:
                pass
        else:
            View.sub_tbl()
            print("\n\n Retour au menu principale.")
            clean()


if __name__ == '__main__':
    main()
