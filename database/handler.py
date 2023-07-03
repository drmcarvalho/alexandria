import sqlite3


def connection():
    return sqlite3.connect("alexandria.db")


def query(con, statement, params=None):
    c = con.cursor()
    try:
        if params is not None:
            c.execute(statement, params)
        else:
            c.execute(statement)
        for row in c:
            yield row
    finally:
        c.close()


def execute(con, statement, params=None):
    c = con.cursor()
    try:
        if params is not None:
            c.execute(statement, params)
        else:
            c.execute(statement)
        con.commit()
    finally:
        c.close()
