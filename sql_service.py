import sqlite3
from sqlalchemy import Integer, String, Column, ForeignKeyConstraint
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///storage.db")
Base = declarative_base()


class Storage(Base):
    __tablename__ = 'storage'
    id = Column(Integer, primary_key=True, )
    name = Column(String(100), nullable=False)
    count_products = Column(Integer, nullable=False, default=1)
    price = Column(Integer, nullable=False)
    size_id = Column(Integer, nullable=False)
    creator_id = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(['size_id'], ['sizes.id']),
        ForeignKeyConstraint(['creator_id'], ['creators.id'])
    )


class Size(Base):
    __tablename__ = 'sizes'
    id = Column(Integer, primary_key=True)
    value = Column(String(100), nullable=False)
    storages = relationship("Storage")


class Creator(Base):
    __tablename__ = 'creators'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    storages = relationship("Storage")


Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


def add_sneaker(name, count, creator, price, size):
    creator_ids = session.query(Creator.id).filter(Creator.name == creator).one_or_none()

    if creator_ids is None:
        print("Такого производителя нет")
        return

    size_ids = session.query(Size.id).filter(Size.value == size).one_or_none()
    if size_ids is None:
        print("Такого размера нет")
        return
    entity = session.query(Storage).filter(Storage.name == name).one_or_none()
    if entity is not None:
        entity.count_products += count
        session.query(Storage).update(entity)
        return True
    entity = Storage(name=name, count_products=count, price=price, size_id=size_ids, creator_id=creator_ids)
    session.add(entity)


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

# # add_sneaker("name", 1, "Nike", 123, 42)
# select_all()
#
# delete_by_name("name")
#
# select_all()
