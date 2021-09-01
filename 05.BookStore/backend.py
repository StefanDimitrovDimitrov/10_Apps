import sqlite3


def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,year integer, author text ,price float)")
    conn.commit()
    conn.close()


def view_all():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM book")

    rows = cur.fetchall()
    conn.close()
    return rows


def search_book(title="", year="", author="", price=""):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR year=? OR author=?  OR price=?", (title, year, author, price))
    rows = cur.fetchall()
    conn.close()
    return rows


def add_book(title, year, author, price):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, year, author, price))

    conn.commit()
    conn.close()


def update_book(id, title, year, author, price):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,year=?,author=?,price=? WHERE id=?",
                (title, year, author, price, id))
    conn.commit()
    conn.close()


def delete_book(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

connect()
