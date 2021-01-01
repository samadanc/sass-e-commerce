from Backend.seller import Seller
from Backend.buyer import Buyer
from Backend.product import Product
from Backend.sale import Sale

users_db = "users.txt"
products_db = "products.txt"
sales_db = "sales.txt"


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
        product_objects.append(Product(product[0], product[1], product[2], product[3]))
    return product_objects


def get_sales():
    sales_objects = []
    with open(sales_db, "r") as db:
        sales_list = [sale.split(",") for sale in db.read().splitlines()]
    for sale in sales_list:
        sale_products = sale[1].strip('[]').split(';')
        sales_objects.append(Sale(sale[0], sale_products, sale[2]))
    return sales_objects


def get_seller_sales(seller):
    sales_objects = []
    with open(sales_db, "r") as db:
        sales_list = [sale.split(",") for sale in db.read().splitlines()]
    for sale in sales_list:
        if sale[0] == seller:
            sale_products = sale[1].strip('[]').split(';')
            sales_objects.append(Sale(sale[0], sale_products, sale[2]))
    return sales_objects


def get_product_discount(product):
    discount = 0
    sales = get_sales()
    for sale in sales:
        for sale_product in sale.get_products():
            if sale_product == product:
                discount = sale.get_discount()
    return discount


def apply_discounts(products):
    sales = get_sales()
    for product in products:
        for sale in sales:
            if product in sale:
                discount = 1-(float(sale.get_discount())/100)
                product.set_price(product.get_price() * discount)


def get_seller_products_with_discount(seller):
    product_objects = []
    with open(products_db, "r") as db:
        products_list = [user.split(",") for user in db.read().splitlines()]
    for product in products_list:
        if product[3] == seller:
            product_objects.append(Product(product[0], product[1], product[2], product[3]))
    apply_discounts(product_objects)
    return product_objects
