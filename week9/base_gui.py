from tkinter import *

class BaseGUI:
    def __init__(self, title, dimensions):
        self._create_window(title, dimensions)
        self._create_widgets()

    def _create_window(self, title, dimensions):
        self._window = Tk()
        self._window.title(title)
        self._window.geometry(dimensions)

    def _create_widgets(self):
        pass  # To be overridden by subclasses

    def run(self):
        self._window.mainloop()