import sqlite3


class LMS:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def ConnectDB(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()

    def CreateTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                    id INTEGER PRIMARY KEY,
                                    title TEXT,
                                    author TEXT,
                                    year INTEGER)''')
        self.conn.commit()

    def AddBook(self, id, title, author, year):
        try:
            self.cursor.execute("INSERT INTO books (id, title, author, year) VALUES (?, ?, ?, ?)",
                                (id, title, author, year))
            self.conn.commit()
            return "Book added successfully!"
        except Exception as e:
            return str(e)

    def UpdateBook(self, id, title, author, year):
        try:
            self.cursor.execute("UPDATE books SET title=?, author=?, year=? WHERE id=?", (title, author, year, id))
            self.conn.commit()
            return "Book updated successfully!"
        except Exception as e:
            return str(e)

    def DeleteBook(self, id):
        try:
            self.cursor.execute("DELETE FROM books WHERE id=?", (id,))
            self.conn.commit()
            return "Book deleted successfully!"
        except Exception as e:
            return str(e)

    def SearchBook(self, search):
        try:
            self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
                                ('%' + search + '%', '%' + search + '%'))
            books = self.cursor.fetchall()
            if books:
                return books
            else:
                return "There is no book matching the search criteria."
        except Exception as e:
            return str(e)