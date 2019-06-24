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
    """Main running function."""
    
    while True:
        res = set_view(View.main_menu, True)
        if res == 1:
            while True:
                cat_id = set_view(View.categories_list)
                if cat_id:
                    while True:
                        prod_id = set_view(lambda: View.products_list(cat_id))
                        if not prod_id:
                            break
                        while True:
                            set_view(lambda: View.product_sheet(prod_id))
                            set_view(lambda: View.prod_sub(prod_id))
                            break
                if not cat_id:
                    break

        elif res == 2:
            set_view(View.sub_tbl)
            res = View.menu("Question:", ["Retour Menu Principale", "Quitter"])
            if not res:
                continue


if __name__ == '__main__':
    
    print("Bienvenue dans ce programme.")    
    main()
