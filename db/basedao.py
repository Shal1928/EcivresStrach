from db.db import get_conn_db, try_exec


class BaseDao:

    def __init__(self, table):
        self.table = table

    def read(self, rowid):
        print('read is not implemented!')

    def readall(self):
        conn = get_conn_db()
        cur = try_exec(conn, 'SELECT ROWID,* FROM main.{}'.format(self.table))
        rows = cur.fetchall()
        conn.close()
        return {key: val for key, val in rows}


class PersistsDao(BaseDao):

    def __init__(self, table):
        super().__init__(self, table)

    def create(self):
        print('create is not implemented!')

    def update(self):
        print('update is not implemented!')

    def delete(self):
        print('delete is not implemented!')
