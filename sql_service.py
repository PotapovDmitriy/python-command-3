from sqlalchemy.orm import sessionmaker

from database import Base, engine
from models import creator, size, sneaker

Creator = creator.Creator
Size = size.Size
Storage = sneaker.Sneaker

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

    count_products = session.query(Storage.count_products).filter(Storage.name == name).one_or_none()
    if count_products is not None:
        session.query(Storage).filter(Storage.name == name). \
            update({"count_products": count_products[0] + count}, synchronize_session="fetch")
    else:
        entity = Storage(name=name, count_products=count, price=price, size_id=size_ids[0], creator_id=creator_ids[0])
        session.add(entity)
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


def add_size(value):
    creator_ids = session.query(Size.id) \
        .filter(Size.value == value) \
        .one_or_none()
    if creator_ids is not None:
        print("Такой размер уже есть")
        return
    entity = Size(value=value)
    session.add(entity)
    session.commit()


def print_all_sneakers():
    entities = session.query(Storage).all()

    for entity in entities:
        size = session.query(Size.value).filter(Size.id == entity.size_id).one_or_none()
        creator = session.query(Creator.name).filter(Creator.id == entity.creator_id).one_or_none()
        print(str(entity) + f"; size: {size[0]}; creator: {creator[0]}")


def select_all_sizes():
    entities = session.query(Size).all()
    return entities


def select_all_creators():
    entities = session.query(Creator).all()
    return entities


def delete_by_name(name):
    storage_id = session.query(Storage.id) \
        .filter(Storage.name == name) \
        .one_or_none()
    if storage_id is None:
        print("Такого товара нет")
        return

    session.query(Storage).filter(Storage.name == name) \
        .delete(synchronize_session="fetch")
