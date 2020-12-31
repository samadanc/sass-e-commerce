from Backend.seller import Seller
from Backend.buyer import Buyer
from Backend.product import Product

users_db = "db/users.txt"
products_db = "db/products.txt"


def save_product(product):
    with open(products_db, "a+") as db:
        db.write(str(product) + '\n')


def save_user(user):
    with open(users_db, "a+") as db:
        db.write(str(user) + '\n')


def get_sellers():
    user_objects = []
    with open(users_db, "r") as db:
        users_list = [user.split(",") for user in db.read().splitlines()]
    for user in users_list:
        if user[2]:
            user_objects.append(Seller(user[0], user[1]))
    return user_objects


def get_buyers():
    user_objects = []
    with open(users_db, "r") as db:
        users_list = [user.split(",") for user in db.read().splitlines()]
    for user in users_list:
        if not user[2]:
            user_objects.append(Buyer(user[0], user[1]))
    return user_objects


def get_users():
    user_objects = []
    with open(users_db, "r") as db:
        users_list = [user.split(",") for user in db.read().splitlines()]
    for user in users_list:
        if user[2]:
            user_objects.append(Seller(user[0], user[1]))
        else:
            user_objects.append(Buyer(user[0], user[1]))
    return user_objects


def get_products():
    product_objects = []
    with open(products_db, "r") as db:
        products_list = [user.split(",") for user in db.read().splitlines()]
    for product in products_list:
        product_objects.append(Product(product[0], product[1], product[2]))
    return product_objects


def get_seller_products(seller):
    product_objects = []
    with open(products_db, "r") as db:
        products_list = [user.split(",") for user in db.read().splitlines()]
    for product in products_list:
        if product[2] == seller:
            product_objects.append(Product(product[0], product[1], product[2]))
    return product_objects
