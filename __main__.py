import tkinter as tk
from tkinter import ttk
from package1.db import try_exec, get_conn_db


def view():
    conn = get_conn_db()

    cur1 = try_exec(conn, '''SELECT ROWID, TITLE FROM main.WORK_TYPE''')
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)

    conn.close()


window = tk.Tk()
window.title("Add Work Record")

tree = ttk.Treeview(window, column=("c1", "c2"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="rowid")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="TITLE")
tree.pack()

button1 = tk.Button(text="Display data", command=view)
button1.pack(pady=10)

window.mainloop()



