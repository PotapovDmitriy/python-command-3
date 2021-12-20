from pydantic import BaseModel
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from database import Base


class Size(Base):
    __tablename__ = 'sizes'
    id = Column(Integer, primary_key=True)
    value = Column(String(100), nullable=False)
    storages = relationship("Sneaker")

    def __str__(self):
        return self.value
