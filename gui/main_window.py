import tkinter as tk
from tkinter import ttk

from gui.commands import get_rwi_widgets


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Add RWI")
        # fields = ["План?", "Тип", "Рамзер", "Заголовок", "Комментарий", "Id"]
        # labels = [tk.Label(self, text=f) for f in fields]
        # entries = [tk.Entry(self) for _ in fields]
        # self.widgets = list(zip(labels, entries))
        self.submit = tk.Button(self, text="Распечатать",
                                command=self.print_info)

        # for i, (label, entry) in enumerate(self.widgets):
        #     label.grid(row=i, column=0, padx=10, sticky=tk.W)
        #     entry.grid(row=i, column=1, padx=10, pady=5)
        get_rwi_widgets(self)
        self.submit.grid(row=3, column=3, sticky=tk.NSEW, padx=10, pady=10)

    def print_info(self):
        for label, entry in self.widgets:
            print("{} = {}".format(label.cget("text"), entry.get()))


# window = tk.Tk()
# window.title("Add Work Record")
#
# tree = ttk.Treeview(window, column=("c1", "c2"), show='headings')
# tree.column("#1", anchor=tk.CENTER)
# tree.heading("#1", text="rowid")
# tree.column("#2", anchor=tk.CENTER)
# tree.heading("#2", text="TITLE")
# tree.pack()
#
# button1 = tk.Button(text="Display data", command=(lambda: view(tree)))
# button1.pack(pady=10)
