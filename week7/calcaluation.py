from tkinter import *
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.__create_window()
        self.__create_widgets()

    def __create_window(self):
        self.window = Tk()
        self.window.title("Simple Calculator")
        self.window.geometry("300x200")

    def __create_widgets(self):
        lbl_a = Label(self.window, text="a:")
        lbl_a.grid(row=0, column=0, padx=10, pady=10, sticky=E)

        self.__a = StringVar()
        entry_a = Entry(self.window, textvariable=self.__a)
        entry_a.grid(row=0, column=1, columnspan=4, padx=10, pady=10, sticky=W)

        lbl_b = Label(self.window, text="b:")
        lbl_b.grid(row=1, column=0, padx=10, pady=10, sticky=E)

        self.__b = StringVar()
        entry_b = Entry(self.window, textvariable=self.__b)
        entry_b.grid(row=1, column=1, columnspan=4, padx=10, pady=10, sticky=W)

        btn_add = Button(self.window, text="+", command=self.__add)
        btn_add.grid(row=2, column=1, padx=5, pady=5)
        btn_sub = Button(self.window, text="-", command=self.__subtract)
        btn_sub.grid(row=2, column=2, padx=5, pady=5)
        btn_mul = Button(self.window, text="*", command=self.__multiply)
        btn_mul.grid(row=2, column=3, padx=5, pady=5)
        btn_div = Button(self.window, text="/", command=self.__divide)
        btn_div.grid(row=2, column=4, padx=5, pady=5)

        lbl_c = Label(self.window, text="c:")
        lbl_c.grid(row=3, column=0, padx=10, pady=10, sticky=E)
        
        self.__c = StringVar()
        entry_c = Entry(self.window, textvariable=self.__c)
        entry_c.grid(row=3, column=1, columnspan=4, padx=10, pady=10, sticky=W)

    def __add(self):
        try:
            a = int(self.__a.get())
            b = int(self.__b.get())
            c = a + b
            self.__c.set(str(c))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for a and b.")

    def __subtract(self):
        try:
            a = int(self.__a.get())
            b = int(self.__b.get())
            c = a - b
            self.__c.set(str(c))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for a and b.")

    def __multiply(self):
        try:
            a = int(self.__a.get())
            b = int(self.__b.get())
            c = a * b
            self.__c.set(str(c))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for a and b.")

    def __divide(self):
        try:
            a = int(self.__a.get())
            b = int(self.__b.get())
            c = a / b
            self.__c.set(str(c))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for a and b.")
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Division by zero is not allowed.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()