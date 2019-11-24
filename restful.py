import sqlite3
from bottle import run, get

emojies = [{'emoji': 'var1'}, {'like': 'var2'}]


@get('/emoji/<emoji>')
def getAll(emoji):
    return {emoji}

@get('/like/<like>/<id>')
def getAll(like, id):
    return {like, id}


run(reloader=True, debug=True)

conn = sqlite3.connect(":memory:")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
cursor.execute("CREATE TABLE data_book(n INTEGER PRIMARY KEY AUTOINCREMENT, author text, rate text, nameofbook text, genre text)")

cursor.execute("INSERT INTO data_book (author, rate, nameofbook) VALUES ('K. Doile','True','Sherlock Holmes','Detective')")
cursor.execute("INSERT INTO data_book (author, rate, nameofbook) VALUES ('W.Shakespeare','False','Hamlet','Tragedy')")
cursor.execute("INSERT INTO data_book (author, rate, nameofbook) VALUES ('J.K. Rowling','False','Harry Potter','Fantastic')")
cursor.execute("INSERT INTO data_book (author, rate, nameofbook) VALUES ('Stephen King','True','IT','Horror')")
cursor.execute("INSERT INTO data_book (author, rate, nameofbook) VALUES ('R.Bradbury','True','451 on Fahrenheit','Sci-Fi')")


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
    cursor.execute("INSERT INTO data_book  (author, rate, nameofbook) VALUES ('J. Austen','True','Persuasion','Novel')")
