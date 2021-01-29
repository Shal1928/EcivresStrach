import tkinter as tk
from package1.db import get_conn_db, try_exec


def view(tree):
    conn = get_conn_db()

    cur1 = try_exec(conn, '''SELECT ROWID, TITLE FROM main.WORK_TYPE''')
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)

    conn.close()
