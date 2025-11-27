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

        self.__lst_books = Listbox(self._window, height=15, width=30, exportselection=False)
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
        # open file dialog to select save location
        books_file = fd.asksaveasfilename(title="Save Books CSV File", defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not books_file:
            messagebox.showwarning("No File Selected", "Select a location to save the CSV file.")
            return
        # open csv file to write books
        writer = csv.writer(open(books_file, 'w', newline=''))
        # write header row
        writer.writerow(['ID', 'Title', 'Author', 'Price'])
        # for each book in the list self.__books, write its details to the csv file
        for book in self.__books:
            writer.writerow([book.book_id, book.title, book.author, book.price])
        messagebox.showinfo("Books Saved", f"Books have been saved successfully to {books_file}")

    def __add_book(self):
        # get title
        title = self.__title_var.get().strip()
        # get author
        author = self.__author_var.get().strip()
        # get price
        price = int(self.__price_var.get().strip())
        # create a new Book object id
        book_id = len(self.__books) + 1
        # create a new Book object
        book = Book(book_id, title, author, price)
        # add the book to the list
        self.__books.append(book)
        # add the book title to the listbox
        self.__lst_books.insert(END, title)
        # show success message
        messagebox.showinfo("Book Added", f"The book '{title}' has been added successfully")


    def __edit_book(self):
        # get the selected index
        index = self.__lst_books.curselection()[0] 
        # get the book from the selected index
        book = self.__books[index]
        # update book details from entry fields
        book.title = self.__title_var.get().strip()
        book.author = self.__author_var.get().strip()
        book.price = float(self.__price_var.get().strip())
        # update the listbox
        self.__lst_books.delete(index)
        self.__lst_books.insert(index, book.title)
        # show success message
        messagebox.showinfo("Book Edited", f"The book '{book.title}' has been updated successfully")

    def __delete_book(self):
        # get the selected index
        index = self.__lst_books.curselection()[0] 
        # delete the book from the list
        book = self.__books.pop(index)
        # delete the book from the listbox
        self.__lst_books.delete(index)
        # clear the entry fields
        self.__title_var.set("")
        self.__author_var.set("")
        self.__price_var.set("")
        # show success message
        messagebox.showinfo("Book Deleted", f"The book '{book.title}' has been deleted successfully")

if __name__ == "__main__":
    app = BookManager()
    app.run()