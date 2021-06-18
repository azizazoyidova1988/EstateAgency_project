from django.db import connection
from contextlib import closing


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from category""")
        categories = dict_fetchall(cursor)
        return categories


def get_categories_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from category""")
        categories_count = dict_fetchall(cursor)
        return categories_count


def get_categories_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  count(product.id),category.name ,product.category_id
        FROM category LEFT JOIN product
		ON product.category_id=category.id
		GROUP BY product.category_id, category.name
        """)
        categories = dict_fetchall(cursor)
        return categories


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from product""")
        products = dict_fetchall(cursor)
        return products


def get_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from product""")
        products_count = dict_fetchall(cursor)
        return products_count


def get_countries():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from country""")
        countries = dict_fetchall(cursor)
        return countries


def get_countries_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from country""")
        countries_count = dict_fetchall(cursor)
        return countries_count


def get_agents():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from agent""")
        agents = dict_fetchall(cursor)
        return agents


def get_agents_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from agent""")
        agents_count = dict_fetchall(cursor)
        return agents_count


def get_news():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from news""")
        news = dict_fetchall(cursor)
        return news


def get_news_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from news""")
        news_count = dict_fetchall(cursor)
        return news_count


def get_testimonials():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from testimonial""")
        testimonials = dict_fetchall(cursor)
        return testimonials


def get_testimonials_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from testimonial""")
        testimonials_count = dict_fetchall(cursor)
        return testimonials_count


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
