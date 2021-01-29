import tkinter as tk
from tkinter import ttk

from gui.commands import get_rwi_fields


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Add RWI")
        fields = get_rwi_fields()
        labels = [tk.Label(self, text=f[0]) for f in fields.values()]
        entries = [tk.Checkbutton(self) if f[1] == 'BOOL' else tk.Entry(self, width=f[2]) for f in fields.values()]
        self.widgets = list(zip(labels, entries))
        self.submit = tk.Button(self, text="Добавить",
                                command=self.print_info)

        for i, (label, entry) in enumerate(self.widgets):
            label.grid(row=0, column=i, padx=10, sticky=tk.W)
            entry.grid(row=1, column=i, padx=10, pady=5)
        self.submit.grid(row=3, column=len(fields)-1, sticky=tk.E,
                         padx=10, pady=10)

    def print_info(self):
        for label, entry in self.widgets:
            print("{} = {}".format(label.cget("text"), entry.get()))
            entry.delete(0, tk.END)


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
