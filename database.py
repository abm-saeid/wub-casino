import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        


def create():
    namelist = """ CREATE TABLE IF NOT EXISTS namelist (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        link text NOT NULL,
                                        balance integer NOT NULL,
                                        hex text NOT NULL
                                    ); """

    storelist = """CREATE TABLE IF NOT EXISTS storelist (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    owner text NOT NULL,
                                    FOREIGN KEY (owner) REFERENCES customer (id)
                                );"""


    conn = create_connection('riches.db')


    if conn is not None:
        create_table(conn, storelist)
        create_table(conn, namelist)
    else:
        print("Error! cannot create the database connection.")
