from tkinter import StringVar, BooleanVar
from model.base import Base, HasComment
from model.rwi import RWI


class TkBase(Base):

    def __init__(self, rowid=None):
        super().__init__(StringVar(), rowid)


class TkHasComment(HasComment):

    def __init__(self, rowid=None):
        self.__init__(StringVar(), StringVar(), rowid)

    def __init__(self, title, comment, rowid=None):
        super().__init__(title, comment, rowid)


class TkRWI(RWI):

    def __init__(self, rowid=None):
        super.__init__(StringVar(), StringVar(), BooleanVar(), TkWorkType(), TkTShirt(), rowid)


class TkWorkType(TkBase):

    def __init__(self, rowid=None):
        super().__init__(rowid)


class TkTShirt(TkBase):

    def __init__(self, rowid=None):
        super().__init__(rowid)
