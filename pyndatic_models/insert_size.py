from pydantic import BaseModel
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship


class InsertSize(BaseModel):
    value: str

    class Config:
        orm_mode = True
