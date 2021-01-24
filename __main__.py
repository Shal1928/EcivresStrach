# from pyquibase.pyquibase import Pyquibase
import sqlite3
from sqlite3 import Error


def init_leadtime_db():
    """ init leadtime db """
    conn = None
    try:
        conn = sqlite3.connect('EcivresStrach/leadtime.sqlite')
        print(sqlite3.version)

        try_exec(conn, '''CREATE TABLE KAS(TITLE TEXT)''')
        try_exec(conn, '''CREATE TABLE TSHIRT(TITLE TEXT)''')
        try_exec(conn, '''CREATE TABLE WORK_TYPE(TITLE TEXT)''')
        try_exec(conn, '''CREATE TABLE RWI
            (TITLE TEXT, COMMENT TEXT, IS_PLAN INTEGER, WORK_TYPE INTEGER, TSHIRT INTEGER)''')
        try_exec(conn, '''CREATE TABLE WORK_RECORD
                    (TITLE TEXT, COMMENT TEXT, START TEXT, FINISH TEXT, KAS INTEGER, RWI INTEGER)''')

        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def try_exec(conn,sql):
    """ Trying executing sql statement """
    try:
        c = conn.cursor()

        c.execute(sql)

        conn.commit()
    except Error as e:
        print(e)


# init_leadtime_db()

# if __name__ == '__main__':
#     pyquibase = Pyquibase.sqlite('test.sqlite', 'sqllite-changelog.sql')
#     pyquibase.update()


