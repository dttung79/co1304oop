from tkinter import *
from tkinter import messagebox

class DemoGUI04:
    def __init__(self):
        self.__create_window()
        self.__create_widgets()
    
    def __create_window(self):
        self.__window = Tk()
        self.__window.title('DEMO GUI 04')
        self.__window.geometry('350x250')

    def __create_widgets(self):
        self.__lbl_choosing = Label(self.__window, text='Choose a product:')
        self.__lbl_choosing.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.__int_product = IntVar()
        self.__int_product.set(2000)    # by default set to iPhone

        self.__rd_iphone = Radiobutton(self.__window, text='iPhone', 
                                       variable=self.__int_product, value=2000, 
                                       command=self.__rd_clicked)
        self.__rd_iphone.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.__rd_samsung = Radiobutton(self.__window, text='Samsung Galaxy', 
                                        variable=self.__int_product, value=1500,
                                        command=self.__rd_clicked)
        self.__rd_samsung.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.__rd_xiaomi = Radiobutton(self.__window, text='Xiaomi Redmi',
                                       variable=self.__int_product, value=1000,
                                       command=self.__rd_clicked)
        self.__rd_xiaomi.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        self.__lbl_payment = Label(self.__window, text='Payment: $2000')
        self.__lbl_payment.grid(row=4, column=0, padx=10, pady=10, sticky=W)

    def __rd_clicked(self):
        payment = self.__int_product.get()
        self.__lbl_payment.config(text='Payment: $' + str(payment))
    
    def run(self):
        self.__window.mainloop()

if __name__ == "__main__":
    app = DemoGUI04()
    app.run()