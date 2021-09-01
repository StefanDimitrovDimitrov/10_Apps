import psycopg2

db = 'db_05_Udemy'
user = 'postgres'
password = '1234qwe'
host = 'localhost'
port = '5432'


def create_table():
    connection = psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port)
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    connection.commit()
    connection.close()


def create_record(item, quantity, price):
    connection = psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port)
    cur = connection.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    connection.commit()
    connection.close()


def view():
    connection = psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port)
    cur = connection.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    connection.close()
    return rows


def delete(item):
    connection = psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port)
    cur = connection.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    connection.commit()
    connection.close()


def update(quantity, price, item):
    connection = psycopg2.connect(dbname=db, user=user, password=password, host=host, port=port)
    cur = connection.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s", (quantity, price, item))
    connection.commit()
    connection.close()


create_table()
create_record("Wine Glass", 100, 100)
update(50, 50, "Wine Glass")
# delete('Book')
# print(view())
