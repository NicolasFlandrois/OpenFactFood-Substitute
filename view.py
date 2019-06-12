#!usr/bin/python3.7
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST
# Author: Nicolas Flandrois

import json
import sqlalchemy as al
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy import create_engine
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

        for num, choice in enumerate(choices):
            print(str(num+1) + " : " + choice)

        while True:
            try:
                choice = int(input())
                if choice in range(1, len(choices)+1):
                    break
                else:
                    raise
            except:
                print(
                    "Veuillez entrer un nombre entre 1 et "
                    + str(len(choices)) + "."
                    )
        print("Vous avez choisi: " + choices[choice-1] + "\n")
        return choice
        # Add possibility to: (R) Return a step back, or (Q) Quit

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

            for sub in resp_sub:
                print("\
Le produit selectionné est:       {}. \n\
EAN-13:                           {}. \n\
Son substitue est:                {}. \n\
Ce produit est-il déjà substitué? {}. \n"
                      .format(product.name, product.ean, sub.name,
                              product.substituted))
                return

    def prod_sub(product_id):
        """View of coresponding product and it's substitute."""
        question = "Voulez vous substituer ce produit? "
        YesNo = ("Oui", "Non")
        resp_prod = session.query(Product).filter(Product.id == product_id)

        for product in resp_prod:
            resp_sub = session.query(Product).filter(Product.id ==
                                                     product.substitute)
            for sub in resp_sub:
                print("\
Produit original: {} \n\
Ce produit a-t-il été déjà substitué? {} \n\
Son produit de substitution est {}".format(product.name, product.substituted,
                                           sub.name))

        choice = View.menu(question, YesNo)

        # Maybe apply here an outside function : substitution_action()
        # if choice == 1:
        #   #Apply substitution's changes
        #   #Apply product.substituted = True
        #   #Apply to sub.id.substituted = False
        # pass

    def SubTbl():
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
