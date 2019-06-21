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

def main():
    """Main running function."""
    clean()
    while True:
        responce = View.main_menu()
        if responce == "r":
            break
        elif responce == "q":
            exit()
        else:
            pass
        clean()  

        if responce == 1:
            category_id = View.categories_list()
            if category_id == "r":
                break
            elif category_id == "q":
                exit()
            else:
                pass
            clean()

            prod_id = View.products_list(category_id)
            if prod_id == "r":
                break
            elif prod_id == "q":
                exit()
            else:
                pass
            clean()
            
            View.product_sheet(prod_id)
            input("Appuyer sur Entrer pour continuer")
            # nextmove = View.menu("Appuyez sur:", 
            #                     ["Continuer",\
            #                     "Retour Menu Principale", "Quitter"])
            # if nextmove in ["r", 2]:
            #     break
            # elif nextmove in ["q", 3]:
            #     exit()
            # else:
            #     pass
            clean()
            
            choice = View.sub_menu()
            if choice == "r":
                break
            elif choice == "q":
                exit()
            else:
                pass
            clean()
            
            if choice == 1:
                View.prod_sub(prod_id)
                # No return_or_quit The choice Not to substitute 
                # needs to be deliberate
                clean()
            else:
                pass

        elif responce == 2:
            View.sub_tbl()
            sub_resp = View.menu("Question:", 
                                ["Retour Menu Principale", "Quitter"])
            if sub_resp in ["r", 1]:
                pass
            elif sub_resp in ["q", 2]:
                exit()
            else:
                pass
            clean()
        
        else:
            pass


if __name__ == '__main__':
    while True:
        main()
