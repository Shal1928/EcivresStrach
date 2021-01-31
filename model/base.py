class Base:

    def __init__(self, title, rowid=None):
        self.title = title
        self.rowid = rowid
        self.test = 'test'


class HasComment(Base):

    def __init__(self, title, comment, rowid=None):
        super().__init__(title, rowid)
        self.comment = comment
