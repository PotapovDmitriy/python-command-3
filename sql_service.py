import sqlite3
from contextlib import closing


def init_db():
    connection = sqlite3.connect('storage.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Creator
                      (Id  INTEGER PRIMARY KEY,
                      Name Text,
                      Country Text)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Size
                      (Id INTEGER PRIMARY KEY,
                      ValueStr Text)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Storage
                      (Id INTEGER PRIMARY KEY,
                      Name Text,
                      CountProducts Int,
                      Price Int,
                      SizeId INTEGER,
                      CreatorId INTEGER,
                      FOREIGN KEY(SizeId) REFERENCES Size,
                      FOREIGN KEY(CreatorId) REFERENCES Creator)''')

    cursor.execute('''INSERT INTO Creator(Name, Country) VALUES ("Nike", "Russia");''')

    cursor.execute('''INSERT INTO Size(ValueStr) VALUES (41)''')
    cursor.execute('''INSERT INTO Size(ValueStr) VALUES (42)''')
    cursor.execute('''INSERT INTO Size(ValueStr) VALUES (43)''')

    print("Инициализация базы прошла успешно")
    connection.commit()
    connection.close()


def add_sneaker(name, count, creator, price, size):
    connection = sqlite3.connect('storage.db')
    cursor = connection.cursor()
    cursor.execute(f'''Select Id from Creator where Name = "{creator}"''')
    creator_ids = cursor.fetchone()
    if creator_ids is None:
        print("Такого производителя нет")
        return

    cursor.execute(f'''Select Id from Size where ValueStr = "{size}"''')
    size_ids = cursor.fetchone()
    if size_ids is None:
        print("Такого размера нет")
        return

    cursor.execute(f'''INSERT INTO Storage(Name, CountProducts, Price, SizeId, CreatorId) 
    VALUES ("{name}", {count}, {price}, {size_ids[0]}, {creator_ids[0]});''')

    connection.commit()
    connection.close()


def select_all():
    connection = sqlite3.connect('storage.db')
    cursor = connection.cursor()
    cursor.execute(f'''SELECT st.Name , st.CountProducts , st.Price , c.Name , s.ValueStr from Storage st, Creator c , Size s
WHERE st.SizeId = s.Id and c.Id = st.CreatorId ;
''')
    sneakers = cursor.fetchall()
    if sneakers is None or len(sneakers) == 0:
        print("Товаров нет")
        return

    for item in sneakers:
        print(item)

    connection.commit()
    connection.close()

def delete_by_name(name):
    connection = sqlite3.connect('storage.db')
    cursor = connection.cursor()
    cursor.execute(f'''Delete from Storage where Name = "{name}"   ''')

    connection.commit()
    connection.close()

# init_db()
# add_sneaker("name", 1, "Nike", 123, 42)
select_all()

delete_by_name("name")

select_all()
