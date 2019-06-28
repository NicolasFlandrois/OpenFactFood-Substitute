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
import os 
import platform
from connection import connect
import time

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
R pour RETOUR au menu précédent.)\n')
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
    def get_off_json(ean:str):
        """Get info from Open Fact Food (off) URL's Json API. Returns a tuple."""
        with urlopen(f"https://world.openfoodfacts.org/api/v0/product/{ean}.json") as response:
            source = response.read()
            data = json.loads(source)

            try:
                quantity = data['product']['quantity']
            except:
                quantity = "-Données indisponibles-"

            try:
                ingredients = data['product']['ingredients_text_fr']
            except:
                ingredients = "-Données indisponibles-"

            return quantity, ingredients

    @staticmethod
    def substitution(prod_id:int):
        """Action to apply Substitution. 
        If not substituted, then apply substitution.
        If already substituted, then reverse substitution."""
        choice = View.submenu_view()
        clean()
        if choice == 1:
            resp_prod = session.query(Product).filter(Product.id == prod_id)
            for prod in resp_prod:
                resp_sub = session.query(Product).filter(Product.id == prod.substitute)
                if not prod.substituted:
                    for sub in resp_sub:
                        prod.substituted = True
                        sub.substituted = False
                        session.commit()
                else:
                    for sub in resp_sub:
                        prod.substituted = False
                        sub.substituted = True
                        session.commit()

            print("La substitution a bien été enregistrer.")
            time.sleep(2)
        else:
            print("Aucune substitution n'a été éffectuée.")
            time.sleep(2)

    @staticmethod
    def sub_tbl_structure(prod_name:str, sub_name:str):
        """This function will display the list of all substituted products in
        the database, along with its matching substitute.
        Data a from real time database."""
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

    @staticmethod
    def sheet_view(prod_id:int):
        """Returns the display for the product's sheet."""
        clean()
        prod_details = View.prod_details(prod_id)
        print(
            f"Le produit selectionné est:       {prod_details['name']}. \n\
EAN-13:                           {prod_details['ean']}. \n\
Poids:                            {prod_details['quantity']}. \n\
\n\
Liste d'ingrédients:\n\
                    {prod_details['ingredients']}. \n\
\n\
Son substitue est:                {prod_details['subname']}. \n\
Ce produit est-il déjà substitué? {prod_details['substatus']}. \n"
            )
        input("\n\nAppuyez sur Entrer pour continuer.")

    @staticmethod
    def status(substituted):
        """Translate the Substituted status True/False into a Yes/No string."""
        for sub in substituted:
            return "Oui" if sub is True else "Non" 

    # Product's Sheet
    product_call = lambda prod_id: session.query(Product).filter(Product.id == prod_id)
    
    def prod_details(prod_id:int):
        """Get all needed prod details for the product's sheet."""
        prod_detail = {}
        prod_detail['name'] = "".join([prod.name for prod in View.product_call(prod_id)])
        prod_detail['ean'] = "".join([prod.ean for prod in View.product_call(prod_id)])
        json_detail = View.get_off_json(prod_detail['ean'])
        prod_detail['quantity'] = json_detail[0]
        prod_detail['ingredients'] = json_detail[1]
        prod_detail['subid'] = int(''.join(map(str, [prod.substitute for prod in View.product_call(prod_id)]))) 
        prod_detail['subname'] = "".join([prod.name for prod in View.product_call(prod_detail['subid'])])
        prod_detail['substatus'] = View.status([prod.substituted for prod in View.product_call(prod_id)])
        return prod_detail

    # Submenu View To choice either we shall substitute or not this product
    submenu_view = lambda: View.menu(
                    "Voulez-vous échanger la substitution de ces produits ? :", [
                        "Oui. Je souhaite échanger la substitution de ces produits ?",
                        "Non. Ne Rien Changer. La situation actuel me convient !"
                       ]
                    )

    # View of substitution table
    @staticmethod
    def sub_tbl ():
        """View of substitution table"""
        sub_prodnames = [prod.name for prod in session.query(Product).filter(Product.substituted == True)]

        sub_subid = [prod.substitute for prod in session.query(Product).filter(Product.substituted == True)]

        sub_subnames = ["".join([prod.name for prod in session.query(Product).filter(Product.id == subid)]) 
                                for subid in sub_subid]

        sub_prodnames_subnames = list(zip(sub_prodnames, sub_subnames))

        clean()
        print("Liste des produits substitués :\n")
        
        for item in sub_prodnames_subnames:
            print(View.sub_tbl_structure(item[0], item[1]))

        input("\n\nAppuyez sur Entrer pour continuer.")
