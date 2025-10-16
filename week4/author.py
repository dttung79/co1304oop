from book import Book

class Author:
    def __init__(self, name):
        self.__name = name
        self.__books = []

    def get_name(self):
        return self.__name
    
    def add_book(self, book):
        self.__books.append(book)

    def show_books(self):
        print(f"Books by {self.__name}:")
        for book in self.__books:
            print(book.get_title())

if __name__ == "__main__":
    jkr = Author("J.K. Rowling") # no books yet
    book1 = Book("Harry Potter and the Sorcerer's Stone", jkr) # jkr now has 1 book
    book2 = Book("Harry Potter and the Chamber of Secrets", jkr) # jkr now has 2 books

    jkr.show_books() # should show 2 books

    print(book1)