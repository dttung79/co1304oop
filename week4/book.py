class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__author.add_book(self)  # Register this book with the author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author
    
    def __str__(self):
        return f'"{self.__title}" by {self.__author.get_name()}'