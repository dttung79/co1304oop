from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from base_gui import BaseGUI
from book import Book
import csv


class BookManager(BaseGUI):
    def __init__(self):
        # call the parent constructor
        super().__init__("Book Manager", "650x400")
        # create an empty list to hold Book objects
        self.__books = []

    def _create_widgets(self):
        btn_load = Button(self._window, text="Load Books", command=self.__load_books)
        btn_load.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.__lst_books = Listbox(self._window, height=15, width=30)
        self.__lst_books.grid(row=1, column=0, padx=10, pady=10, sticky=W, rowspan=4)
        # bind the listbox selection event to a method
        self.__lst_books.bind('<<ListboxSelect>>', self.__show_a_book)

        btn_save = Button(self._window, text="Save Books", command=self.__save_books)
        btn_save.grid(row=5, column=0, padx=10, pady=10, sticky=W)

        lbl_title = Label(self._window, text="Title:")
        lbl_title.grid(row=1, column=1, padx=10, pady=5, sticky=E)
        
        self.__title_var = StringVar()
        txt_title = Entry(self._window, width=25, textvariable=self.__title_var)
        txt_title.grid(row=1, column=2, padx=10, pady=5, sticky=W, columnspan=3)

        lbl_author = Label(self._window, text="Author:")
        lbl_author.grid(row=2, column=1, padx=10, pady=5, sticky=E)

        self.__author_var = StringVar()
        txt_author = Entry(self._window, width=25, textvariable=self.__author_var)
        txt_author.grid(row=2, column=2, padx=10, pady=5, sticky=W, columnspan=3)

        lbl_price = Label(self._window, text="Price:")
        lbl_price.grid(row=3, column=1, padx=10, pady=5, sticky=E)

        self.__price_var = StringVar()
        txt_price = Entry(self._window, width=25, textvariable=self.__price_var)
        txt_price.grid(row=3, column=2, padx=10, pady=5, sticky=W, columnspan=3)

        btn_add = Button(self._window, text="Add", command=self.__add_book)
        btn_add.grid(row=4, column=2, padx=10, pady=10, sticky=W)

        btn_edit = Button(self._window, text="Edit", command=self.__edit_book)
        btn_edit.grid(row=4, column=3, padx=10, pady=10, sticky=W)

        btn_del = Button(self._window, text="Delete", command=self.__delete_book)
        btn_del.grid(row=4, column=4, padx=10, pady=10, sticky=W)

        btn_exit = Button(self._window, text="Exit", width=20, command=self._window.quit)
        btn_exit.grid(row=5, column=2, padx=10, pady=10, sticky=W, columnspan=3)

    def __show_a_book(self, event):
        # get the selected index
        index = self.__lst_books.curselection()[0] 
        # get the book
        book = self.__books[index]
        # display book details in the entry fields
        self.__title_var.set(book.title)
        self.__author_var.set(book.author)
        self.__price_var.set(str(book.price))
        
    def __load_books(self):
        books_file = fd.askopenfilename(title="Select Books CSV File", filetypes=[("CSV files", "*.csv")])
        if not books_file:
            messagebox.showwarning("No File Selected", "Please select a CSV file to load books.")
            return
        # open csv file to read books
        reader = csv.reader(open(books_file, newline=''))
        next(reader)  # skip header row
        self.__books.clear() # clear existing books
        # for each row, create a Book object and add to the list
        for row in reader:
            book_id, title, author, price = row
            book = Book(book_id, title, author, float(price))
            self.__books.append(book)

        self.__show_books()

    def __show_books(self):
        # clear the listbox
        self.__lst_books.delete(0, END)
        # for each book in the list self.__books, insert its title into the listbox
        for book in self.__books:
            title = book.title
            self.__lst_books.insert(END, title) # insert only the title

    def __save_books(self):
        pass

    def __add_book(self):
        pass

    def __edit_book(self):
        pass

    def __delete_book(self):
        pass

if __name__ == "__main__":
    app = BookManager()
    app.run()