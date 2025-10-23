from tkinter import *
from tkinter import messagebox

class DemoGUI02:
    def __init__(self):
        self.__create_window()
        self.__create_widgets()
    
    def __create_window(self):
        self.__window = Tk()
        self.__window.title("Demo GUI 02")
        self.__window.geometry("300x200")
    
    def __create_widgets(self):
        self.__label = Label(self.__window, text='Label text')
        self.__label.grid(row=0, column=0, padx=10, pady=10)

        self.__str = StringVar()
        self.__str.set("Entry text")
        self.__entry = Entry(self.__window, width=20, textvariable=self.__str)
        self.__entry.grid(row=1, column=0, padx=10, pady=10)

        self.__button = Button(self.__window, text="Switch text", command=self.__button_clicked)
        self.__button.grid(row=2, column=0, padx=10, pady=10)
        
    def __button_clicked(self):
        # get label text
        label_text = self.__label.cget("text")  # direct way to get label text
        # get entry text
        entry_text = self.__str.get()           # indirect way to get entry text via StringVar
        # switch texts
        self.__label.config(text=entry_text)    # direct way to set label text
        self.__str.set(label_text)      # indirect way to set entry text via StringVar  
        # show message box
        messagebox.showinfo("Info", "Texts switched!")

    def run(self):
        self.__window.mainloop()

if __name__ == "__main__":
    app = DemoGUI02()
    app.run()