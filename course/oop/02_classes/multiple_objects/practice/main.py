class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book_to_remove):
        new_books = []
        for book in self.books:
            if not (book.title == book_to_remove.title and book.author == book_to_remove.author):
              new_books.append(book)
        self.books = new_books

    def search_books(self, search_string):
        matched_books = []
        search_lower = search_string.lower()
        for book in self.books:
            if search_lower in book.title.lower() or search_lower in book.author.lower():
              matched_books.append(book)
        return matched_books

