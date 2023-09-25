from sqlalchemy.sql import text
from models.connect import engine

# SQL문 사용 방법
with engine.connect() as con:

    data = ( { "id": 1, "title": "The Hobbit", "primary_author": "Tolkien" },
             { "id": 2, "title": "The Silmarillion", "primary_author": "Tolkien" },
    )

    statement = text("""INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)""")

    for line in data:
        con.execute(statement, **line)


with engine.connect() as con:

    rs = con.execute('SELECT * FROM book')

    for row in rs:
        print(row)