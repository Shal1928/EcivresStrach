import tkinter as tk
from package1.db import get_conn_db, try_exec


def get_rwi_fields():
    # conn = get_conn_db()

    # cur1 = try_exec(conn, '''SELECT * FROM main.RWI''')
    # rwi_fields = {}
    return {
        'IS_PLAN': ('Плановая?', 'BOOL', None),
        'TSHIRT': ('Размер', 'STR*', 5),
        'WORK_TYPE': ('Тип работы', 'STR*', 10),
        'TITLE': ('Заголовок', 'STR', 30),
        'COMMENT': ('Комментарий', 'STR', 30),
        'ID': ('ID', 'STR', 10)
    }
    # for d in cur1.description:
    #     if d ==
    #
    # return tuple(tuple(d[0], 'S') if 'IS_PLAN' for d in cur1.description)
    # for f in fields:
    #     print(f)

    # for row in rows:
    #     print(row)
    #     tree.insert("", tk.END, values=row)

    # conn.close()
