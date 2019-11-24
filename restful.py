import sqlite3
from bottle import run, get

conn = sqlite3.connect(":memory:")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE data_book(n INTEGER PRIMARY KEY AUTOINCREMENT, author text, rate text, nameofbook text, genre text)")

cursor.execute(
    "INSERT INTO data_book (author, rate, nameofbook, genre) VALUES ('K. Doile','True','Sherlock Holmes','1')")
cursor.execute("INSERT INTO data_book (author, rate, nameofbook, genre) VALUES ('W.Shakespeare','False','Hamlet','2')")
cursor.execute(
    "INSERT INTO data_book (author, rate, nameofbook, genre) VALUES ('J.K. Rowling','False','Harry Potter','3')")
cursor.execute("INSERT INTO data_book (author, rate, nameofbook, genre) VALUES ('Stephen King','True','IT','4')")
cursor.execute(
    "INSERT INTO data_book (author, rate, nameofbook, genre) VALUES ('R.Bradbury','True','451 on Fahrenheit','5')")

emojies = [{'emoji': 'var1'}, {'like': 'var2'}]


@get('/emoji/<emoji>')
def getAll(emoji):
    print(connect(emoji))


@get('/like/<like>/<id>')
def getAll(like, id):
    return {like, id}


def connect(emoji):
    sql = "SELECT * FROM data_book WHERE genre=?"
    cursor.execute(sql, [emoji])
    return cursor.fetchall()


run(reloader=True, debug=True)


# функция выводит всю БД
def database_get_all():
    for row in cursor.execute("SELECT * FROM data_book"):
        print(row)


# функция получает и выводит все книги с положительным рейтингом
def database_get():
    sql = "SELECT * FROM data_book WHERE rate=?"
    cursor.execute(sql, [("True")])
    print(cursor.fetchall())


# функция меняет все отрицательные(или неотмеченные) отзывы, на положительные
def database_change():
    sql = "UPDATE data_book SET rate = 'True' WHERE rate = 'False'"

    cursor.execute(sql)
    conn.commit()


# функция добавления еще одной книги(по сути, она не нужна, т.к. все мы книги мы сами забиваем)
def database_add():
    cursor.execute(
        "INSERT INTO data_book  (author, rate, nameofbook, genre) VALUES ('J. Austen','True','Persuasion','Novel')")
