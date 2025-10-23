from tkinter import *
from tkinter import messagebox

class DemoGUI05:
    def __init__(self):
        self.__create_window()
        self.__create_widgets()
    
    def __create_window(self):
        self.__window = Tk()
        self.__window.title('DEMO GUI 05')
        self.__window.geometry('350x250')

    def __create_widgets(self):
        self.__lbl_choosing = Label(self.__window, text='Choose product(s):')
        self.__lbl_choosing.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.__bool_iphone = BooleanVar()
        self.__cb_iphone = Checkbutton(self.__window, text='iPhone ($2000)',
                                        variable=self.__bool_iphone,
                                        command=self.__rd_clicked)
        self.__cb_iphone.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.__bool_samsung = BooleanVar()
        self.__cb_samsung = Checkbutton(self.__window, text='Samsung Galaxy ($1500)',
                                         variable=self.__bool_samsung,
                                         command=self.__rd_clicked)
        self.__cb_samsung.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.__bool_xiaomi = BooleanVar()
        self.__cb_xiaomi = Checkbutton(self.__window, text='Xiaomi Redmi ($1000)',
                                        variable=self.__bool_xiaomi,
                                        command=self.__rd_clicked)
        self.__cb_xiaomi.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        self.__lbl_payment = Label(self.__window, text='Payment: $0')
        self.__lbl_payment.grid(row=4, column=0, padx=10, pady=10, sticky=W)

    def __rd_clicked(self):
        total_payment = 0
        if self.__bool_iphone.get() == True:
            total_payment += 2000
        if self.__bool_samsung.get() == True:
            total_payment += 1500
        if self.__bool_xiaomi.get() == True:
            total_payment += 1000

        self.__lbl_payment.config(text='Payment: $' + str(total_payment))

    def run(self):
        self.__window.mainloop()

if __name__ == "__main__":
    app = DemoGUI05()
    app.run()