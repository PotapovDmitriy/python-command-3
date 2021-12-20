from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

import connection

Base = connection.Base


class Creator(Base):
    __tablename__ = 'sizes'
    id = Column(Integer, primary_key=True)
    value = Column(String(100), nullable=False)
    storages = relationship("Storage")
