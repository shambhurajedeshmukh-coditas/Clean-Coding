from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of the Book class can be added.")

    def search_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def search_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        return found_books

    def total_books(self):
        return len(self.books)

    def display_books(self):
        if self.books:
            for book in self.books:
                print(book.get_details())
        else:
            print("No books available in the library.")

