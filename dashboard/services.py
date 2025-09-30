from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_category():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from food_category""")
        categories = dictfetchall(cursor)
        return categories


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT food_product.id, food_product.title, food_category.title as category
         from food_product left join food_category on food_product.category_id = food_category.id
         """)
        products = dictfetchall(cursor)
        return products


def get_customer():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from food_customer""")
        customer = dictfetchall(cursor)
        return customer


def get_orders():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT food_order.id, food_order.customer, food_order.address,
        food_order.payment_type, food_customer.first_name as customer_first_name from 
        food_order left join food_customer on food_order.customer_id = food_customer.id
        """)
        orders = dictfetchall(cursor)
        return orders
