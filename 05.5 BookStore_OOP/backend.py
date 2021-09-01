import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('books')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book"
            " (id INTEGER PRIMARY KEY,title text,year integer, author text ,price float)")
        self.conn.commit()

    def view_all(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search_book(self, title="", year="", author="", price=""):
        self.conn = sqlite3.connect('books')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM book WHERE title=? OR year=? OR author=?  OR price=?", (title, year, author, price))
        rows = self.cur.fetchall()
        return rows

    def add_book(self, title, year, author, price):
        self.conn = sqlite3.connect('books')
        self.cur = self.conn.cursor()

        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, year, author, price))
        self.conn.commit()

    def update_book(self, id, title, year, author, price):
        self.conn = sqlite3.connect('books')
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE book SET title=?,year=?,author=?,price=? WHERE id=?",
                    (title, year, author, price, id))
        self.conn.commit()

    def delete_book(self, id):
        self.conn = sqlite3.connect('books')
        self.cur = self.conn.cursor()
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()