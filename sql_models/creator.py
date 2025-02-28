from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from database import Base


class Creator(Base):
    __tablename__ = 'creators'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    storages = relationship("Sneaker")

    def __str__(self):
        return self.name
