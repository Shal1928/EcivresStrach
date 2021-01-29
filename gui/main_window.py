import tkinter as tk
from tkinter import ttk

from gui.commands import view

window = tk.Tk()
window.title("Add Work Record")

tree = ttk.Treeview(window, column=("c1", "c2"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="rowid")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="TITLE")
tree.pack()

button1 = tk.Button(text="Display data", command=(lambda: view(tree)))
button1.pack(pady=10)

window.mainloop()
