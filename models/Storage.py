from sqlalchemy import Integer, String, Column, ForeignKeyConstraint

import connection

Base = connection.Base


class Storage(Base):
    __tablename__ = 'storage'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    count_products = Column(Integer, nullable=False, default=1)
    price = Column(Integer, nullable=False)
    size_id = Column(Integer, nullable=False)
    creator_id = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(['size_id'], ['sizes.id']),
        ForeignKeyConstraint(['creator_id'], ['creators.id'])
    )
