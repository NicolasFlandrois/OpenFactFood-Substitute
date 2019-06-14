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

with open("config.json") as f:
    config = json.load(f)

username = config["username"]
password = config["password"]
host = config["host"]
port = config["port"]

engine = create_engine(
    f'mysql+pymysql://{username}:{password}@{host}/off1?host={host}?port=\
    {port}', echo=False, encoding='utf8', pool_recycle=60000,
    pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()


class View(object):
    """Views to display various infos needed through software's cicles."""

    def menu(question, choices):
        """skeleton menu's view for each query and set of question"""

        print(question)
        print('(Appuyer sur: Q pour quitter ou R pour retour en arrière.)')

        for num, choice in enumerate(choices):
            print(str(num+1) + " : " + choice)

        while True:
            try:
                choice = input()
                if choice.strip().lower() in ['r', 'q']:
                    print(f'test1 You choose: {choice}')
                    break
                else:
                    choice = int(choice)
                    if choice in range(1, len(choices)+1):
                        print("Vous avez choisi: " + choices[choice-1] + "\n")
                        break
                    else:
                        raise
            except:
                print(
                    "Veuillez entrer un nombre entre 1 et " +
                    str(len(choices)) + "."
                    )

        return choice

    def categories_list():
        """View of all categories."""
        question = "Veuillez choisir une catégorie: "
        categoryList = []
        categoryQuery = session.query(Category).all()

        for choice in categoryQuery:
            categoryList.append(str(choice))

        return View.menu(question, categoryList)

    def products_list(cat_id):
        """View of all products within a category."""
        question = "Veuillez choisir un produit : "
        productList = []
        product_ids = []
        response = session.query(Product).filter(Product.category == cat_id)

        for product in response:
            productList.append(product.name)
            product_ids.append(product.id)

        return product_ids[View.menu(question, productList)-1]

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
                return

    def prod_sub(product_id):
        """View of coresponding product and it's substitute."""
        question = "Voulez vous substituer ce produit? "
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
{product.name}\n\
Ce produit est substitué par:\n\
    {sub.name}\n")
