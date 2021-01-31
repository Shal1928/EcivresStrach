class Base:

    def __init__(self, title, rowid=None):
        self.title = title
        self.rowid = rowid
        self.test = 'test'

    @property
    def rowid(self):
        return self.rowid


class WorkType(Base):

    def __init__(self, title, rowid=None):
        self.__init__(title, rowid)


class TShirt(Base):

    def __init__(self, title, rowid=None):
        self.__init__(title, rowid)


class HasComment(Base):

    def __init__(self, title, comment, rowid=None):
        self.__init__(title, rowid)
        self.comment = comment
