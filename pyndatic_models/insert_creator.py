from pydantic import BaseModel


class InsertCreator(BaseModel):
    name: str
    country: str

    class Config:
        orm_mode = True
