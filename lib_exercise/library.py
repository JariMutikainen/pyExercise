# Implement a library system, which supports the following tasks:
# 1. Show all the books available in the library
# 2. Borrow a book from the library
# 3. Return a book into the library

class Book:
    def __init__(self, title):
        self.title = title
        self.in_shelf = True

class Library:
    def __init__(self):
        self.books = [Book('Rambo 1'), Book('Rambo 2'), Book('Rambo 3')]

    def show_books(self):
        print('\nThe books available in the library are:')
        for book in self.books:
            if book.in_shelf:
                print(book.title)

    def borrow_book(self, bookname):
        for book in self.books:
            if bookname == book.title:
                print(f'\nYou borrowed {book.title} now.')
                book.in_shelf = False
                return
        print(f'\n{bookname} is not available in the library')
        return

    def return_book(self, bookname):
        for book in self.books:
            if bookname == book.title:
                print(f'\nYou returned {book.title} now.')
                book.in_shelf = True
                return
        print(f'\n{bookname} does not belong to this library')
        return

# Testing
lib1 = Library()
lib1.show_books()
lib1.borrow_book('Rambo 2')
lib1.show_books()
lib1.borrow_book('Alice in the wonderland')
lib1.show_books()
lib1.return_book('Rambo 2')
lib1.show_books()

