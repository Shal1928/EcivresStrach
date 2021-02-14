from store import Session
from store.dbo import WorkType, TShirt


class BaseDS:

    def __init__(self, dao):
        self.session = Session()
        self.dao = dao
        self.table = dao.__tablename__

    def all(self):
        return self.session.query(self.dao)


class WorkTypeDS(BaseDS):

    def __init__(self):
        super().__init__(WorkType)


class TShirtDS(BaseDS):

    def __init__(self):
        super().__init__(TShirt)
