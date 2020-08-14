from books_app import BooksApp
from db.adapter import BooksDBAdapter

if __name__=="__main__":
    adapter = BooksDBAdapter()
    app = BooksApp(adapter)
    app.start()