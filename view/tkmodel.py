from tkinter import StringVar, BooleanVar, IntVar


def init_var(t, value):
    is_none = value is None
    return {
        str: StringVar() if is_none else value,
        int: IntVar() if is_none else value,
        bool: BooleanVar() if is_none else value
    }[t]


def observe(*args):
    print('Observe!')
    print(args)


class TkBase:

    def __init__(self,
                 rowid=None, title=None):
        self.rowid = rowid
        self.title = init_var(str, title)
        self.title.trace('w', observe)

    def __safe_get_rowid__(self):
        return self.rowid if self.rowid is None else self.rowid.get()

    def __str__(self):
        return f'{self.title.get()!r}'

    def __repr__(self):
        return \
            f'{self.__class__.__name__}('\
            f'{self.__safe_get_rowid__()!r}, '\
            f'{self.title.get()!r})'


class TkHasComment(TkBase):

    def __init__(self,
                 rowid=None, title=None,
                 comment=None):
        super().__init__(rowid, title)
        self.comment = init_var(str, comment)


class TkWorkType(TkBase):
    def __init__(self,
                 rowid=None, title=None):
        self.rowid = rowid
        self.title = init_var(str, title)


class TkTShirt(TkBase):
    def __init__(self,
                 rowid=None, title=None):
        self.rowid = rowid
        self.title = init_var(str, title)


class TkRWI(TkHasComment):

    def __init__(self,
                 rowid=None, title=None,
                 comment=None,
                 is_plan=None, work_type=None, tshirt=None, pid=None, master=None, customer=None, cp=None, ddd=None):
        super().__init__(rowid, title, comment)
        self.is_plan = init_var(bool, is_plan)
        self.work_type = work_type
        self.tshirt = tshirt
        self.pid = init_var(str, pid)
        self.master = master
        self.customer = init_var(str, customer)
        self.cp = cp
        self.ddd = ddd

    def __str__(self):
        return \
            f'title={self.title.get()}, ' \
            f'comment={self.comment.get()}, ' \
            f'is plan={self.is_plan.get()}, ' \
            f'work type={self.work_type}, ' \
            f't-shirt={self.tshirt}, ' \
            f'pid={self.pid.get()}, ' \
            f'master={self.master}, '\
            f'customer={self.customer.get()}, ' \
            f'cp={self.cp}, ' \
            f'ddd={self.ddd}'

    def __repr__(self):
        return \
            f'{self.__class__.__name__}('\
            f'rowid={self.__safe_get_rowid__()!r}, '\
            f'title={self.title.get()!r}, '\
            f'comment={self.comment.get()!r}, '\
            f'is plan={self.is_plan.get()!r}, '\
            f'work type={self.work_type!r}, '\
            f't-shirt={self.tshirt!r}, '\
            f'pid={self.pid.get()!r}, '\
            f'master={self.master!r}, '\
            f'customer={self.customer.get()!r}, ' \
            f'cp={self.cp!r}, ' \
            f'ddd={self.ddd!r}'
