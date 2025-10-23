from tkinter import *
from tkinter import messagebox

class IELTSCalculate:
    def __init__(self):
        self.__create_window()
        self.__create_widgets()
    
    def __create_window(self):
        self.__window = Tk()
        self.__window.title('IELTS Score Calculator')
        self.__window.geometry('350x250')

    def __create_widgets(self):
        self.__lbl_reading = Label(self.__window, text='Reading Score:')
        self.__lbl_reading.grid(row=0, column=0, padx=10, pady=10)

        self.__str_reading = StringVar()
        self.__entry_reading = Entry(self.__window, width=10, textvariable=self.__str_reading)
        self.__entry_reading.grid(row=0, column=1, padx=10, pady=10)

        self.__lbl_writing = Label(self.__window, text='Writing Score:')
        self.__lbl_writing.grid(row=1, column=0, padx=10, pady=10)

        self.__str_writing = StringVar()
        self.__entry_writing = Entry(self.__window, width=10, textvariable=self.__str_writing)
        self.__entry_writing.grid(row=1, column=1, padx=10, pady=10)

        self.__lbl_listening = Label(self.__window, text='Listening Score:')
        self.__lbl_listening.grid(row=2, column=0, padx=10, pady=10)

        self.__str_listening = StringVar()
        self.__entry_listening = Entry(self.__window, width=10, textvariable=self.__str_listening)
        self.__entry_listening.grid(row=2, column=1, padx=10, pady=10)

        self.__lbl_speaking = Label(self.__window, text='Speaking Score:')
        self.__lbl_speaking.grid(row=3, column=0, padx=10, pady=10)

        self.__str_speaking = StringVar()
        self.__entry_speaking = Entry(self.__window, width=10, textvariable=self.__str_speaking)
        self.__entry_speaking.grid(row=3, column=1, padx=10, pady=10)

        self.__btn_calculate = Button(self.__window, text='Calculate', command=self.__calculate_score)
        self.__btn_calculate.grid(row=4, column=1, padx=10, pady=10)

        self.__lbl_result = Label(self.__window, text='Overall Score: ')
        self.__lbl_result.grid(row=5, column=0, padx=10, pady=10)

        self.__str_result = StringVar()
        self.__entry_result = Entry(self.__window, width=10, textvariable=self.__str_result)
        self.__entry_result.grid(row=5, column=1, padx=10, pady=10)

    def __calculate_score(self):
        reading = float(self.__str_reading.get())
        writing = float(self.__str_writing.get())
        listening = float(self.__str_listening.get())
        speaking = float(self.__str_speaking.get())

        avg_score = (reading + writing + listening + speaking) / 4
        # round up .25 to .5 and .75 to next integer
        if 0 <= avg_score - int(avg_score) <= 0.35:
            overall_score = int(avg_score)
        elif 0.35 < avg_score - int(avg_score) <= 0.5:
            overall_score = int(avg_score) + 0.5
        elif 0.5 < avg_score - int(avg_score) <= 0.85:
            overall_score = int(avg_score) + 0.5
        else:
            overall_score = round(avg_score) + 1    
        
        self.__str_result.set(str(overall_score))

    def run(self):
        self.__window.mainloop()

if __name__ == '__main__':
    app = IELTSCalculate()
    app.run()