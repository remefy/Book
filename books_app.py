from db.adapter import BooksDBAdapter
from models import Book


class BooksApp:
    def __init__(self, adapter: BooksDBAdapter):
        self.adapter = adapter

    def start(self):
        self.adapter.prepare()
        self._mainloop()

    def _mainloop(self):
        while True:
            command = input("\nВведите команду или напишите help:\n>>")
            if command == "help":
                print("exit - Выйти из программы")
                print("show all - Показать все книги")
                print("add - добавить книгу")
                print("delete - Удалить книгу")
            elif command == "exit":
                print("Пока!")
                break
            elif command == "show all":
                books = self.adapter.get_all_books()
                for book in books:
                    print(book)
            elif command == "add":
                name = input("\nОк, введите назвние книги: ")
                year = int(input("Введите год книги: "))
                author = input("Введите автор книги: ")
                book = Book(name, year, author, "Fiction")
                self.adapter.save_new_book(book)
                print("Книга доблена успешно")
            elif command == "delete":
                id = int(input("Введите id книги: "))
                book = self.adapter.get_book_by_id(id)
                if book is not None:
                    self.adapter.delete_book(book)
                    print("Книга удалена успешно")
                else:
                    print("Книга не найдена")
            else:
                print(f"Команда {command} не найдена")
