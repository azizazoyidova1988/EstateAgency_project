from django.db import connection
from contextlib import closing


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from category""")
        categories = dict_fetchall(cursor)
        return categories


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*,category.name as cat_name,
        country.name as country_name from product left join category on product.category_id=category.id 
        left join country on product.country_id = country.id """)
        products = dict_fetchall(cursor)
        return products


def get_product_by_rent():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*,category.name as cat_name,
        country.name as country_name from product left join category on product.category_id=category.id 
        left join country on product.country_id = country.id where status = 'rent'""")
        pro_rent = dict_fetchall(cursor)
        return pro_rent


def get_product_by_sale():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*,category.name as cat_name,
        country.name as country_name from product left join category on product.category_id=category.id 
        left join country on product.country_id = country.id where status = 'sale'""")
        pro_sale = dict_fetchall(cursor)
        return pro_sale


def get_product_by_created_at():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*,category.name as cat_name,
        country.name as country_name from product left join category on product.category_id=category.id 
        left join country on product.country_id = country.id order by created_at desc""")
        pro_new = dict_fetchall(cursor)
        return pro_new


def get_products_by_id(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*,category.name as cat_name,
        country.name as country_name from product left join category on product.category_id=category.id 
        left join country on product.country_id = country.id where product.id=%s """, [product_id])
        product = dict_fetchone(cursor)
        return product


def get_latest_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*,category.name as cat_name,
        country.name as country_name from product left join category on product.category_id=category.id 
        left join country on product.country_id = country.id 
        where product.price < 1200 order by product.price Desc""")
        lat_products = dict_fetchall(cursor)
        return lat_products



def get_services():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from services """)
        services = dict_fetchall(cursor)
        return services


def get_agents():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from agent """)
        agents = dict_fetchall(cursor)
        return agents


def get_agent(agent_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from agent where agent.id=%s""", [agent_id])
        agent = dict_fetchone(cursor)
        return agent


def get_news():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select news.*, category.name as c_name from news left join category 
        on news.category_id = category.id order by created_at limit 3 """)
        news = dict_fetchall(cursor)
        return news


def get_news_by_id(news_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select news.*, category.name as c_name from news left join category 
        on news.category_id = category.id where news.id=%s """, [news_id])
        new = dict_fetchone(cursor)
        return new


def get_posts():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select news.*, category.name as c_name from news left join category 
        on news.category_id = category.id  """)
        posts = dict_fetchall(cursor)
        return posts


def get_testimonials():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from testimonial """)
        testimonials = dict_fetchall(cursor)
        return testimonials


def get_commenter():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from commenter """)
        commenter = dict_fetchall(cursor)
        return commenter


def get_countries():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from country """)
        countries = dict_fetchall(cursor)
        return countries


def get_amenities():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from amenities """)
        amenities = dict_fetchall(cursor)
        return amenities


def get_mini_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select mini_category.*, category.name as c_name from mini_category
            inner join category on mini_category.category_id = category.id """)
        mini_categories = dict_fetchall(cursor)
        return mini_categories


def get_product_details(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select products.*, brands.name as b_name from products
            inner join brands on products.brands_id = brands.id
            where products.id =  %s""", [product_id])
        mini_categories = dict_fetchone(cursor)
        return mini_categories



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
