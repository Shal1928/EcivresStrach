import tkinter as tk
from gui.commands import get_rwi_widgets


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Add RWI")
        # self.rwi = TkRWI()
        get_rwi_widgets(self)
        tk.Button(self,
                  text="Добавить RWI",
                  command=self.add_rwi
                  ).grid(row=3, column=3, sticky=tk.NSEW, padx=10, pady=10)

    def add_rwi(self):
        for label, entry in self.widgets:
            print("{} = {}".format(label.cget("text"), entry.get()))
