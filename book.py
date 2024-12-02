class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"

    def update_details(self, title=None, author=None, publication_year=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if publication_year:
            self.publication_year = publication_year
