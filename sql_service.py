from sqlalchemy.orm import sessionmaker

from database import Base, engine
from sql_models import creator, size, sneaker

Creator = creator.Creator
Size = size.Size
Sneaker = sneaker.Sneaker

Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


def add_sneaker(sneaker : Sneaker):
    creator_ids = session.query(Creator.id).filter(Creator.id == sneaker.creator_id).one_or_none()
    if creator_ids is None:
        print("Такого производителя нет")
        return

    size_ids = session.query(Size.id).filter(Size.id == sneaker.size_id).one_or_none()
    if size_ids is None:
        print("Такого размера нет")
        return

    count_products = session.query(Sneaker.count_products).filter(Sneaker.name == sneaker.name).one_or_none()
    if count_products is not None:
        session.query(Sneaker).filter(Sneaker.name == sneaker.name). \
            update({"count_products": count_products[0] + sneaker.count_products}, synchronize_session="fetch")
    else:
        session.add(sneaker)
    session.commit()


def add_creator(name, country):
    creator_ids = session.query(Creator.id) \
        .filter(Creator.name == name, Creator.country == country) \
        .one_or_none()
    if creator_ids is not None:
        print("Такой производитель уже есть")
        return
    entity = Creator(name=name, country=country)
    session.add(entity)
    session.commit()


def add_size(size: Size):
    creator_ids = session.query(Size.id) \
        .filter(Size.value == size.value) \
        .one_or_none()
    if creator_ids is not None:
        return "Такой размер уже есть"
    session.add(size)
    session.commit()


def get_all_sneakers():
    return session.query(Sneaker).all()

    # for entity in entities:
    #     size = session.query(Size.value).filter(Size.id == entity.size_id).one_or_none()
    #     creator = session.query(Creator.name).filter(Creator.id == entity.creator_id).one_or_none()
    #     print(str(entity) + f"; size: {size[0]}; creator: {creator[0]}")


def get_sneakers_by_name(name):
    return session.query(Sneaker) \
        .filter(Sneaker.name == name) \
        .one_or_none()


def get_sneakers_by_id(id):
    return session.query(Sneaker) \
        .filter(Sneaker.id == id) \
        .one_or_none()


def select_all_sizes():
    entities = session.query(Size).all()
    return entities


def select_all_creators():
    entities = session.query(Creator).all()
    return entities


def delete_by_id(id):
    result = session.query(Sneaker).filter(Sneaker.id == id) \
        .delete(synchronize_session="fetch")

    session.commit()
    return result
