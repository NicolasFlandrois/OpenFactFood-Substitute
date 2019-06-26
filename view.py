#!/usr/bin/python3.7
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST
# Author: Nicolas Flandrois

import json
from urllib.request import urlopen
import sqlalchemy as al
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy import create_engine, update
from models import Product, Category
import os, platform
from connection import connect

session = connect()

def clean():
    """This function will clear the terminal's screen. The command is 
    automaticaly detected according to the system OS you run it.
    Compatible with Windows, OSx, and Linux."""
    os.system("cls" if platform.system() == "Windows" else "clear")


class View(object):
    """Views to display various infos needed through software's cycles."""

    @staticmethod
    def menu(question, choices=None):
        """skeleton menu's view for each query and set of question."""
        clean()
        print(question)
        if choices:
            for num, choice in enumerate(choices):
                print(str(num+1) + " : " + choice)
        print('\n(Appuyer sur: Q pour QUITTER ou \
R pour RETOUR au menu principal.)\n')
        while True:
            try:
                choice = input()
                if choice.strip().lower() in ['r', 'q']:
                    break
                elif choices:
                    choice = int(choice)
                    if choice in range(1, len(choices)+1):
                        break
                    else:
                        raise
            except:
                print(
                    "Veuillez entrer un nombre entre 1 et " +
                    str(len(choices)) + "."
                    )

        return choice
    
    @staticmethod
    def get_off_json(ean):
        """Get info from Open Fact Food (off) URL's Json API."""
        with urlopen(f"https://world.openfoodfacts.org/api/v0/product/{ean}.json") as response:
            source = response.read()

            data = json.loads(source)

            try:
                quantity = data['product']['quantity']
            except:
                quantity = "-Données indisponible-"

            try:
                ingredients = data['product']['ingredients_text_fr']
            except:
                ingredients = "-Données indisponible-"

            return quantity, ingredients

    @staticmethod
    def status(substituted):
        """Translate the Substituted status True/False into a Yes/No string."""
        return "Oui" if substituted is True  else "Non"

    @staticmethod
    def sheet_structure(name, ean, quantity, ingredients, subname, substatus):
        """Returns the display for the product's sheet."""
        print(
            f"Le produit selectionné est:       {name}. \n\
EAN-13:                           {ean}. \n\
Poids:                            {quantity}. \n\
\n\
Liste d'ingrédients:\n\
                    {ingredients}. \n\
\n\
Son substitue est:                {subname}. \n\
Ce produit est-il déjà substitué? {substatus}. \n"
            )

    @staticmethod
    def substitution(product_id):
        """Action to apply Substitution"""
        get_prod(product_id).substituted = True
        get_prod(product_id).substitute.substituted = False
        session.commit()
        return "La substitution a bien été enregistrer."

    # @staticmethod
    # def get_allsub():
    #     return session.query(Product).filter(Product.substituted == True)

    @staticmethod
    def sub_tbl_structure(prods):
        """This function will display the list of all substituted products in
        the database, along with its matching substitute.
        Data a from real time database."""
        print("Liste des produits substitués en ce moment, et leurs substitus.\n")
        for prod in prods:
            print(f"\
{prod.name} (Non utilisé)\n\
    Ce produit est substitué par:\n\
    {prod.substitue.name} (Utilisé).\n"
    )


    # Shows Main Menu (Beginning Menu)
    main_view = lambda: View.menu(
        "Entrez votre choix:", [
            "Naviguer vers un produit.",
            "Afficher la liste de tous les produits substitués en ce moment."
        ]
    )

    # Shows a list of all available catgories, and returns user's category's choice
    cats_view = lambda: View.menu(
        "Veuillez choisir une catégorie: ", [
            (cat.id, cat.name) for cat in session.query(Category).all()
        ]
    )

    # Shows the list of all products within this category, and returns user's product's choice
    prods_view = lambda cat_id: View.menu(
        "Veuillez choisir un type de produits : ", [
            (prod.id, prod.name) for prod in session.query(Product).filter(Product.category == cat_id)
        ]
    )

    prod_view = lambda prod_id: View.sheet_structure(
            str(prod.name for prod in session.query(Product).filter(Product.category == prod_id)),
            str(prod.ean for prod in session.query(Product).filter(Product.category == prod_id)),
            str(View.get_off_json(
                prod.ean for prod in session.query(Product).filter(Product.category == prod_id))[0]),
            str(View.get_off_json(
                prod.ean for prod in session.query(Product).filter(Product.category == prod_id))[1]),
            str(prod.substitute.name for prod in session.query(Product).filter(Product.category == prod_id)),
            str(View.status(
                prod.substituted for prod in session.query(Product).filter(Product.category == prod_id))
            )
        )                

    submenu_view = lambda: View.menu(
                                    "Voulez-vous :", [
                                        "Substituer ce produit ?",
                                        "Retour au menu principal ?"
                                       ]
                                    )

    sub_tbl = lambda: View.sub_tbl_structure(
        prod for products in session.query(Product).filter(Product.substituted == True)
        )


# TEST
# View.main_view() # ok
# View.submenu_view() # ok

# View.cats_view()
    # Issue: Veuillez choisir une catégorie: 
    # Traceback (most recent call last):
    #   File "view.py", line 167, in <module>
    #     View.cats_view()
    #   File "view.py", line 137, in <lambda>
    #     (cat.id, cat.name) for cat in session.query(Category).all()
    #   File "view.py", line 34, in menu
    #     print(str(num+1) + " : " + choice)
    # TypeError: can only concatenate str (not "tuple") to str

# View.prods_view(2)
    # Veuillez choisir un type de produits : 
    # Traceback (most recent call last):
    #   File "view.py", line 176, in <module>
    #     View.prods_view(2)
    #   File "view.py", line 138, in <lambda>
    #     (prod.id, prod.name) for prod in session.query(Product).filter(Product.category == cat_id)
    #   File "view.py", line 34, in menu
    #     print(str(num+1) + " : " + choice)
    # TypeError: can only concatenate str (not "tuple") to str

# View.prod_view(2)
    # <generator object View.<lambda>.<locals>.<genexpr> at 0x7f3f53d6f0c0>
    # <generator object View.<lambda>.<locals>.<genexpr> at 0x7f3f53d740c0>
    # -Données indisponible-
    # -Données indisponible-
    # <generator object View.<lambda>.<locals>.<genexpr> at 0x7f3f53d890c0>
    # Non
    # Le produit selectionné est:       None. 
    # EAN-13:                           None. 
    # Poids:                            None. 

    # Liste d'ingrédients:
    #                     None. 

    # Son substitue est:                None. 
    # Ce produit est-il déjà substitué? None.

# View.sub_tbl()
    # Liste des produits substitués en ce moment, et leurs substitus.
    # Traceback (most recent call last):
    #   File "view.py", line 207, in <module>
    #     View.sub_tbl()
    #   File "view.py", line 161, in <lambda>
    #     sub_tbl = lambda: View.sub_tbl_structure(prod for products in session.query(Product).filter(Product.substituted == True))
    #   File "view.py", line 114, in sub_tbl_structure
    #     for prod in prods:
    #   File "view.py", line 161, in <genexpr>
    #     sub_tbl = lambda: View.sub_tbl_structure(prod for products in session.query(Product).filter(Product.substituted == True))
    # NameError: name 'prod' is not defined

