import tkinter as tk

from db.rwidao import WorkTypeDao, TShirtDao
from gui.custom.advcombobox import Advcombobox
from model.rwi import WorkType, TShirt


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
    work_type = WorkTypeDao()
    tshirt = TShirtDao()
    wt = work_type.table
    ts = tshirt.table
    return {
        'IS_PLAN': get_frame(m, 'Плановая?', 'check', tk.TOP, []).grid(row=0, column=0, padx=10, pady=5, sticky=tk.EW),
        wt: get_frame(
            m, 'Тип работы', 'combo', tk.TOP, work_type.readall()
        ).grid(
            row=0, column=1, padx=10, pady=5, sticky=tk.EW
        ),
        ts: get_frame(
            m, 'Размер', 'combo', tk.TOP, tshirt.readall()
        ).grid(
            row=0, column=2, padx=10, pady=5, sticky=tk.EW
        ),
        'ID': get_frame(m, 'Id', 'entry', tk.TOP, []).grid(row=0, column=3, padx=10, pady=5, sticky=tk.EW),
        'TITLE': get_frame(m, 'Заголовок', 'entry', tk.TOP, []).grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky=tk.EW),
        'COMMENT': get_frame(m, 'Комментарий', 'entry', tk.TOP, []).grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky=tk.EW)
    }
