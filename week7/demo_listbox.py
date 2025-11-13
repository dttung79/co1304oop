from tkinter import *
from tkinter import messagebox

class DemoListbox:
    def __init__(self):
        # List of programming languages
        self.__languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "Swift"]
        self.__difficulties = ["Easy", "Medium", "Hard", "Medium", "Easy", "Medium", "Hard"]
        self.__create_window()
        self.__create_widgets()

    def __create_window(self):
        self.__window = Tk()
        self.__window.title("Demo Listbox")
        self.__window.geometry("300x300")

    def __create_widgets(self):
        lbl_title = Label(self.__window, text="Select a Programming Language:")
        lbl_title.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.__lst_languages = Listbox(self.__window, height=6)
        self.__lst_languages.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        # bind listbox to a handler
        self.__lst_languages.bind("<<ListboxSelect>>", self.__language_selected)

        self.__load_languages()

        lbl_lang_selected = Label(self.__window, text="You selected:")
        lbl_lang_selected.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        self.__selected_language = StringVar()
        txt_selected_language = Entry(self.__window, textvariable=self.__selected_language)
        txt_selected_language.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        lbl_difficulty = Label(self.__window, text="Difficulty Levels:")
        lbl_difficulty.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        self.__difficulty = StringVar()
        self.__txt_difficulty = Entry(self.__window, textvariable=self.__difficulty)
        self.__txt_difficulty.grid(row=5, column=0, padx=10, pady=5, sticky=W)

    def __language_selected(self, event):
        # get selected index
        sel_index = self.__lst_languages.curselection()[0]
        # from selected index, get the language
        sel_language = self.__languages[sel_index]
        # set the selected language to the StringVar to update the Entry widget
        self.__selected_language.set(sel_language)
        # set difficulty level
        sel_difficulty = self.__difficulties[sel_index]
        self.__difficulty.set(sel_difficulty)

    def __load_languages(self):
        # go through the list and insert each language into the Listbox
        for language in self.__languages:
            self.__lst_languages.insert(END, language)

    def run(self):
        self.__window.mainloop()

if __name__ == "__main__":
    demo = DemoListbox()
    demo.run()