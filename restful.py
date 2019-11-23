import sqlite3
from bottle import run, get

emojies = [{'emoji': 'var1'}, {'like': 'var2'}]


@get('/emoji/<emoji>/<like>')
def getAll(emoji, like):
    return {emoji, like}


run(reloader=True, debug=True)


conn = sqlite3.connect("memory")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
cursor.execute("CREATE TABLE data_book(n INTEGER PRIMARY KEY, author text, rate text, nameofbook text)")


cursor.execute("INSERT INTO data_book VALUES (0,'tolstoy','true','voyna i mir')")
cursor.execute("INSERT INTO data_book VALUES (1,'pushkin','true','voyna i NE mir')")
cursor.execute("INSERT INTO data_book VALUES (2,'tolstoy','true','voyna i NE mir')")
cursor.execute("INSERT INTO data_book VALUES (3,'tolstoy','true','voyna i NE mir')")
cursor.execute("INSERT INTO data_book VALUES (4,'tolstoy','true','voyna i NE mir')")


def database_get():
    sql = "SELECT * FROM data_book WHERE author=?"
    cursor.execute(sql, [("pushkin")])
    print(cursor.fetchall())


def database_change():
    sql = "UPDATE data_book SET author = 'Konan Doile' WHERE author = 'tolstoy'"

    cursor.execute(sql)
    conn.commit()


"""def database_add():
    cursor.execute("INSERT INTO data_book VALUES (id,'tolstoy','true','voyna i NE mir')")"""

