from tkinter import *

class DemoGUI01:
    def __init__(self):
        # create a window
        self.__window = Tk()
        self.__window.title("Demo GUI 01")
        self.__window.geometry("300x200")

        # create some widgets
        self.__label = Label(self.__window, text="Hello, GUI World!")
        self.__label.grid(row=0, column=0, padx=10, pady=10)

        self.__button = Button(self.__window, text="Click Me", command=self.__button_clicked)
        self.__button.grid(row=1, column=0, padx=10, pady=10)

    def __button_clicked(self):
        self.__label.config(text="Button Clicked!")

    def run(self):
        self.__window.mainloop()

if __name__ == "__main__":
    app = DemoGUI01()
    app.run()
