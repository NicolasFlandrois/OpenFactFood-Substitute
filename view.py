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
        """Get info from Open Fact Food (off) URL's Json API. Returns a tuple."""
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

            return quantity, ingredients # returns a tuple

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

    @staticmethod
    def sub_tbl_structure(prod_name, sub_name):
        """This function will display the list of all substituted products in
        the database, along with its matching substitute.
        Data a from real time database."""
        # print("Liste des produits substitués en ce moment, et leurs substitus.\n")
        return f"{prod_name} (Non utilisé)\n\
    Ce produit est substitué par:\n\
    {sub_name} (Utilisé).\n"


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
            cat.name for cat in session.query(Category).all()
        ]
    )

    # Shows the list of all products within this category, and returns user's product's choice
    prods_view = lambda cat_id: View.menu(
        "Veuillez choisir un type de produits : ", [
            prod.name for prod in session.query(Product).filter(Product.category == cat_id)
        ]
    )

    # Product's Sheet
    product_call = lambda prod_id: session.query(Product).filter(Product.category == prod_id)
    
    def product2sheet(prod_id):
        prod_details = []
        for label in View.product_call(prod_id):
            prod_details.append(label)
        return prod_details

    prod_view = lambda prod_id: View.sheet_structure(
                    View.product2sheet(prod_id)[2],
                    View.product2sheet(prod_id)[1],
                    (View.get_off_json(View.product2sheet(prod_id)[1])[0]),
                    (View.get_off_json(View.product2sheet(prod_id)[1])[1]),
                    View.product_call(View.product2sheet(prod_id)[4]),
                    (View.status(View.product2sheet(prod_id)[5]))
                )

    submenu_view = lambda: View.menu(
                                    "Voulez-vous :", [
                                        "Substituer ce produit ?",
                                        "Retour au menu principal ?"
                                       ]
                                    )

    # Preparing lists for substitution table
    sub_prodnames = [prod.name for prod in session.query(Product).filter(Product.substituted == True)]

    sub_subid = [prod.substitute for prod in session.query(Product).filter(Product.substituted == True)]

    sub_subnames = [[prod.name for prod in session.query(Product).filter(Product.id == subid)] 
                            for subid in sub_subid]

    sub_prodnames_subnames = list(zip(sub_prodnames, sub_subnames))

    @staticmethod
    def sub_tbl (prod_sub_names:list):
        print("Liste des produits substitués : ")
        for item in prod_sub_names:
            print(View.sub_tbl_structure(item[0], item[1]))

# TEST
# View.main_view() # ok
# View.submenu_view() # ok
# print(View.sub_prodnames_subnames) # OK
# View.sub_tbl(View.sub_prodnames_subnames) # OK
# View.cats_view() # OK
# View.prods_view(2) # OK

# print(View.product2sheet(2))

View.prod_view(2)
# Issues