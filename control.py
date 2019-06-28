#!/usr/bin/python3.7
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST
# Author: Nicolas Flandrois

from sys import exit
from models import Product, Category
from view import View


def set_view(view, top_level=False):
    res = view()
    if res == "r":
        if top_level:
            exit()
        else:
            return None
    elif res == "q":
        exit()
    else:
        return res


def main():
    """Program's Main running function."""
    
    while True:
        res = set_view(View.main_view, True)
        # ISSUE: When in Top menu main_view(), "r" and "q" for Return/Quit commands doesn't work. Quit == OK || Return == Quit but it shouldn't
        if res == 1:
            while True:
                cat_id = set_view(View.cats_view)
                if cat_id:
                    while True:
                        prod_id = set_view(lambda: View.prods_view(cat_id))
                        if not prod_id:
                            break
                        while True:
                            set_view(lambda: View.sheet_view(prod_id))
                            set_view(lambda: View.substitution(prod_id))
                            # ISSUE: When in substitution()'s sub menu, the choice is: 1 to apply substitution, 2 to not apply sub, r to return to the previous menu, q to quit >>> However, Quit reacts like a return command... It should Quit/Exit the program
                            break
                if not cat_id:
                    break

        elif res == 2:
            set_view(View.sub_tbl)
            res = View.menu("Question:", ["Retour Menu Principale", "Quitter"])
            # ISSUE: When finishing visualising the sub_tbl() (after clicking enter to continue) the "q" for Quit command don't work. Instead of Quitting/Exiting the program, it actually returns to the main_view() as a return command.
            if not res:
                continue


if __name__ == '__main__':
    
    print("Bienvenue dans ce programme.")    
    main()
