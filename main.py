from books_app import BooksApp
from db.sqlite_adapter import SqliteBooksDBAdapter

if __name__ == "__main__":
    adapter = SqliteBooksDBAdapter("books.sqlite3")
    app = BooksApp(adapter)
    app.start()
