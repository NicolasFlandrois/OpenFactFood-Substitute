#!usr/bin/python3.7
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
    automaticaly detected according to the system OS you run it."""
    os.system("cls" if platform.system() == "Windows" else "clear")


class View(object):
    """Views to display various infos needed through software's cycles."""

    @static_method
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

    main_view = lambda: View.menu(
        "Entrez votre choix:", [
            "Naviguer vers un produit.",
            "Afficher la liste de tous les produits substitués en ce moment."
        ]
    )

    cats_view = lambda: View.menu(
        "Veuillez choisir une catégorie: ", [
            (cat.id, cat.name) for cat in session.query(Category).all()
        ]
    )

    prods_view = lambda cat_id: View.menu(
        "Veuillez choisir un produit : ", [
            (prod.id, prod.name) for prod in session.query(Product).filter(Product.category == cat_id)
        ]
    )

    prod_view = lambda prod_id: View.menu(
        "Veuillez choisir un produit : ", [
            (prod.id, prod.name) for prod in session.query(Product).filter(Product.category == cat_id)
        ]
    )

    @static_method
    def product_sheet(product_id):
        """View of a specific product's ID and informations. Product sheet."""
        response = session.query(Product).filter(Product.id == product_id)

        for product in response:
            resp_sub = session.query(Product).filter(Product.id ==
                                                     product.substitute)

            with urlopen(f"https://world.openfoodfacts.org/api/v0/product/\
                         {product.ean}.json") as response:
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

            if product.substituted is True:
                substituted = "Oui"
            else:
                substituted = "Non"

            for sub in resp_sub:
                print(f"\
Le produit selectionné est:       {product.name}. \n\
EAN-13:                           {product.ean}. \n\
Poids:                            {quantity}. \n\
\n\
Liste d'ingrédients:\n\
{ingredients}. \n\
\n\
Son substitue est:                {sub.name}. \n\
Ce produit est-il déjà substitué? {substituted}. \n")
                input("Appuyez sur une touche pour continuer...")

    @static_method
    def sub_menu():
        """This function will display the sub menu of the program."""
        question = "Voulez-vous :"
        choices = ["Substituer ce produit ?",
                   "Retour au menu principal ?"]
        return View.menu(question, choices)

    @static_method
    def prod_sub(product_id):
        """View of coresponding product and it's substitute."""
        question = "Confirmez-vous la substitution de ce produit? "
        YesNo = ("Oui", "Non")
        resp_prod = session.query(Product).filter(Product.id == product_id)

        for product in resp_prod:
            resp_sub = session.query(Product).filter(Product.id ==
                                                     product.substitute)

            if product.substituted is True:
                substituted = "Oui"
            else:
                substituted = "Non"

            for sub in resp_sub:
                print(f"\
Produit original: {product.name} \n\
Ce produit a-t-il été déjà substitué? {substituted} \n\
Son produit de substitution est {sub.name}")

        choice = View.menu(question, YesNo)

        # Maybe apply here an outside function : substitution_action()
        if choice == 1:
            # Apply substitution's changes
            product.substituted = True

            sub.substituted = False

            session.commit()
            print("La substitution a bien été enregistrer.")

    @static_method
    def sub_tbl():
        """This function will display the list of all substituted products in
        the database, along with its matching substitute.
        Data a from real time database.

                 (Col 0)              (Col 1)
        +----------------------+--------------------+
        |Subststituted product | Current Substitute |
        +======================+====================+
        | Product A   (True)   | Prod Sub-A (False) |
        +----------------------+--------------------+
        | Product B            | Product Sub-B      |
        +----------------------+--------------------+
        | Product C            | Product Sub-C      |
        +----------------------+--------------------+
        | Product etc...       | Sub - etc...       |
        +----------------------+--------------------+

        Display in column 0, all products for which Substituted == True.
        Display in column 1, all corresponding products to substitution."""
        print("Liste des produits substitués en ce moment, et leurs substitus.")
        resp_prod = session.query(Product).filter(Product.substituted == True)

        for product in resp_prod:
            resp_sub = session.query(Product).filter(Product.id ==
                                                     product.substitute)
            for sub in resp_sub:
                print(f"\n\
{product.name} (Non utilisé)\n\
    Ce produit est substitué par:\n\
    {sub.name} (Utilisé).\n")
        input("Appuyez sur une touche pour continuer...")

