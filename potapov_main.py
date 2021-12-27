import uvicorn

import sql_service as sql
from fastapi import FastAPI

from pyndatic_models.insert_creator import InsertCreator
from pyndatic_models.insert_size import InsertSize
from pyndatic_models.insert_sneaker import InsertSneaker
from sql_models.creator import Creator

from sql_models.size import Size
from sql_models.sneaker import Sneaker

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/getAllSneakers")
async def get_all_sneakers():
    return sql.get_all_sneakers()


@app.get("/getSneakerById/{item_id}")
async def get_all_sneakers(item_id):
    return sql.get_sneakers_by_id(item_id)


@app.get("/getSneakerByName/{name}")
async def get_all_sneakers(name):
    return sql.get_sneakers_by_name(name)


@app.get("/getAllSizes")
async def select_all_sizes():
    return sql.select_all_sizes()


@app.get("/getAllCreators")
async def select_all_creators():
    return sql.select_all_creators()


@app.delete("/deleteSneakerById/{id}")
async def delete_sneaker_by_id(id):
    return sql.delete_by_id(id)


@app.post("/addSize")
async def add_size(size: InsertSize):
    return sql.add_size(Size(value=size.value))


@app.post("/addCreator")
async def add_creator(creator: InsertCreator):
    return sql.add_creator(Creator(name=creator.name, country=creator.country))


@app.post("/addSneaker")
async def add_sneaker(sneaker: InsertSneaker):
    return sql.add_sneaker(Sneaker(name=sneaker.name, count_products=sneaker.count_products, size_id=sneaker.size_id,
                                   creator_id=sneaker.creator_id, price=sneaker.price))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)