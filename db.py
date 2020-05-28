import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def namelist(conn, names):
    sql = ''' INSERT INTO namelist(name,link,balance,hex)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, names)
    return


def entry(names):
    conn = create_connection('riches.db')
    with conn:
        if len(names)==4:
            namelist(conn,names)
        else:
            return True

def select_all_names(conn):
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('select * from namelist WHERE NOT id=41 ORDER BY balance DESC')
    rows = c.fetchall()
    return rows

def transactions():
    conn = create_connection('riches.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("select * from namelist where id=41")
    rows = c.fetchall()
    return rows


def find(name):
    conn = create_connection('riches.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    sql="select * from namelist where name LIKE ?"
    command=[f"%{name}%"]
    c.execute(sql, command)
    rows = c.fetchall()
    return rows

def findhex(hex):
    conn = create_connection('riches.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    sql="select * from namelist where hex LIKE ?"
    command=[f"%{hex}%"]
    c.execute(sql, command)
    rows = c.fetchall()
    return rows


def search():
    conn = create_connection('riches.db')
    with conn:
        return select_all_names(conn)


def increment(id_num, amount):
    conn=create_connection('riches.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    id_num=[f"%{id_num}%"]
    if amount>0:
        c.execute(f"UPDATE namelist SET balance=balance+{amount} WHERE hex LIKE ?", id_num)
    elif amount<0:
        amount=abs(amount)
        c.execute(f"UPDATE namelist SET balance=balance-{amount} WHERE hex LIKE ?", id_num)
    c.execute(f"UPDATE namelist SET balance=balance+{amount} WHERE id=41")
    c.execute("select * from namelist where hex LIKE ?", id_num)
    rows = c.fetchall()
    conn.commit()
    return rows