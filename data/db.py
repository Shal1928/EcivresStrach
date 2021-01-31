import sqlite3
from sqlite3 import Error
# from pyquibase.pyquibase import Pyquibase


def get_conn_db():
    conn = None
    try:
        conn = sqlite3.connect('EcivresStrach/leadtime.sqlite')
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)


def init_leadtime_db():
    """ init leadtime db """
    conn = None
    try:
        conn = get_conn_db()

        try_exec(conn, '''CREATE TABLE KAS(TITLE TEXT)''', True)
        try_exec(conn, '''CREATE TABLE TSHIRT(TITLE TEXT)''', True)
        try_exec(conn, '''CREATE TABLE WORK_TYPE(TITLE TEXT)''', True)
        try_exec(conn, '''CREATE TABLE RWI
            (TITLE TEXT, COMMENT TEXT, IS_PLAN INTEGER, WORK_TYPE INTEGER, TSHIRT INTEGER, ID TEXT)''', True)
        try_exec(conn, '''CREATE TABLE WORK_RECORD
                    (TITLE TEXT, COMMENT TEXT, START TEXT, FINISH TEXT, KAS INTEGER, RWI INTEGER)''', True)

        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def try_exec(conn, sql, is_commit=False):
    """ Trying executing sql statement """
    try:
        c = conn.cursor()

        c.execute(sql)

        if is_commit:
            conn.commit()

        return c
    except Error as e:
        print(e)

# init_leadtime_db()

# if __name__ == '__main__':
#     pyquibase = Pyquibase.sqlite('test.sqlite', 'sqllite-changelog.sql')
#     pyquibase.update()