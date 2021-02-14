from tkinter import Tk, TOP, EW, NSEW, Button, StringVar, IntVar, NE, NW, NS
from tkinter.ttk import Radiobutton

from store.ds import WorkTypeDS, TShirtDS
from view.tkmodel import TkRWI, TkWorkType, TkTShirt
from view.common import get_frame


class RWIWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Add RWI")
        self.rwi = TkRWI(work_type=TkWorkType(rowid=1), tshirt=TkTShirt(rowid=0), cp=StringVar(), ddd=StringVar())

        # Column 0
        work_type = WorkTypeDS()
        get_frame(
            self,
            'Тип работы', 'radio_group',
            TOP,
            self.rwi.work_type,
            {row.rowid: row.title for row in work_type.all()}
        ).grid(
            column=0, row=0,
            columnspan=1, rowspan=6,
            padx=10, pady=5,
            sticky=NW
        )

        # Column 1&2
        get_frame(
            self,
            'Плановая?', 'check',
            TOP,
            self.rwi.is_plan
        ).grid(
            column=1, row=0,
            columnspan=2, rowspan=1,
            padx=10, pady=5,
            sticky=EW
        )

        get_frame(
            self,
            'Заголовок', 'entry',
            TOP,
            self.rwi.title
        ).grid(
            column=1, row=1,
            columnspan=2, rowspan=1,
            padx=10, pady=5,
            sticky=EW
        )

        get_frame(
            self,
            'Комментарий', 'entry',
            TOP,
            self.rwi.comment
        ).grid(
            column=1, row=2,
            columnspan=2, rowspan=1,
            padx=10, pady=5,
            sticky=EW
        )

        get_frame(
            self,
            'Заказчик', 'entry',
            TOP,
            self.rwi.customer
        ).grid(
            column=1, row=3,
            columnspan=2, rowspan=1,
            padx=10, pady=5,
            sticky=EW
        )

        get_frame(
            self,
            'Точка принятия обязательств', 'date',
            TOP,
            self.rwi.cp
        ).grid(
            column=1, row=4,
            columnspan=1, rowspan=1,
            padx=10, pady=5,
            sticky=EW
        )

        get_frame(
            self,
            'Желаемая дата поставки', 'date',
            TOP,
            self.rwi.ddd
        ).grid(
            column=2, row=4,
            columnspan=1, rowspan=1,
            padx=10, pady=5,
            sticky=EW
        )

        get_frame(
            self,
            'Системный идентификатор', 'entry',
            TOP,
            self.rwi.pid
        ).grid(
            column=1, row=5,
            columnspan=2, rowspan=1,
            padx=10, pady=5,
            sticky=NS
        )

        Button(
            self,
            text="Добавить RWI",
            command=self.add_rwi
        ).grid(
            column=1, row=6,
            columnspan=2, rowspan=1,
            padx=10, pady=5,
            sticky=NS
        )

        # Column 3
        tshirt = TShirtDS()
        ts_dic = {0: '?'}
        ts_dic.update({row.rowid: row.title for row in tshirt.all()})
        get_frame(
            self,
            'Размер', 'radio_group',
            TOP,
            self.rwi.tshirt,
            ts_dic
        ).grid(
            column=3, row=0,
            columnspan=1, rowspan=5,
            padx=30, pady=5,
            sticky=NW
        )

    def add_rwi(self):
        print(f'{self.rwi}')


