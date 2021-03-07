class Book:

    def __init__(self, ISBN, title, used):
        self._ISBN = ISBN
        self._title = title
        self._owner = "Biblioteque Brossard"
        self._used = used

    def get_isbn(self):
        return self._ISBN

    def set_title(self, title):
        self._title = title

    def get_title(self):
        return self._title



book1 = Book("123456789", "War of the Worlds", False)
book1.set_title("Some other title")
book2 = Book("234567890", "Insomnia", False)
book3 = Book(None, "Insomnia Part 2", True)
array_of_books = [book1, book2, book3]

