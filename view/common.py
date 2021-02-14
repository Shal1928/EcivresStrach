import datetime
import tkinter as tk
from tkinter import LEFT, X, TOP, W

from tkcalendar import DateEntry
from view.custom.advcombobox import Advcombobox
from view.custom.advdateentry import AdvDateEntry


def get_frame(m, t, entry_type, s, var, val=None):
    f = tk.Frame(m)
    label = tk.Label(f, text=t)
    label.pack(side=s, anchor=tk.W)

    if entry_type == 'entry':
        tk.Entry(f, textvariable=var)\
            .pack(side=s, fill=tk.X)
    elif entry_type == 'check':
        tk.Checkbutton(f, variable=var, text=t)\
            .pack(side=s, fill=tk.X)
        label.config(text='')
    elif entry_type == 'radio_group':
        for key, v in val.items():
            tk.Radiobutton(f, text=v, value=key, variable=var).pack(side=s, anchor=W)
    elif entry_type == 'combo':
        Advcombobox(f, values=val, textvariable=var)\
            .pack(side=s, fill=tk.X)
    elif entry_type == 'date':
        AdvDateEntry(f, textvar=var,
                     foreground='white', borderwidth=0, locale='ru_RU', date_pattern='dd.MM.YYYY')\
            .pack(side=s, fill=tk.X)
    else:
        print(f'entry_type = {entry_type} is unknown!')

    return f
