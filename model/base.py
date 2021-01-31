class Base:

    def __init__(self, title, rowid=None):
        self.title = title
        self.rowid = rowid
        self.test = 'test'

    @property
    def rowid(self):
        return self.rowid


class HasComment(Base):

    def __init__(self, title, comment, rowid=None):
        super().__init__(title, rowid)
        self.comment = comment
