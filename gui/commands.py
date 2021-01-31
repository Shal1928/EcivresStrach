import tkinter as tk
from gui.custom.advcombobox import Advcombobox
from data.db import get_conn_db, try_exec


def get_db_data(table):
    conn = get_conn_db()
    cur = try_exec(conn, 'SELECT ROWID,* FROM main.{}'.format(table))
    rows = cur.fetchall()
    conn.close()
    print(rows)
    print({key: val for key, val in rows})
    return {key: val for key, val in rows}


def get_frame(m, t, entry_type, s, data):
    f = tk.Frame(m)
    tk.Label(f, text=t).pack(side=s, anchor=tk.W)
    {
        'entry': tk.Entry(f),
        'check': tk.Checkbutton(f),
        'combo': Advcombobox(f, values=data)
    }[entry_type].pack(side=s, fill=tk.X)
    return f


def get_rwi_widgets(m):
    wt = 'WORK_TYPE'
    ts = 'TSHIRT'
    return {
        'IS_PLAN': get_frame(m, 'Плановая?', 'check', tk.TOP, []).grid(row=0, column=0, padx=10, pady=5, sticky=tk.EW),
        wt: get_frame(
            m, 'Тип работы', 'combo', tk.TOP, get_db_data(wt)
        ).grid(
            row=0, column=1, padx=10, pady=5, sticky=tk.EW
        ),
        ts: get_frame(
            m, 'Размер', 'combo', tk.TOP, get_db_data(ts)
        ).grid(
            row=0, column=2, padx=10, pady=5, sticky=tk.EW
        ),
        'ID': get_frame(m, 'Id', 'entry', tk.TOP, []).grid(row=0, column=3, padx=10, pady=5, sticky=tk.EW),
        'TITLE': get_frame(m, 'Заголовок', 'entry', tk.TOP, []).grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky=tk.EW),
        'COMMENT': get_frame(m, 'Комментарий', 'entry', tk.TOP, []).grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky=tk.EW)
    }
