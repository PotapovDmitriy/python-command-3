from pydantic import BaseModel


class InsertSneaker(BaseModel):
    name: str
    count_products: int
    price: int
    size_id: int
    creator_id: int

    class Config:
        orm_mode = True
