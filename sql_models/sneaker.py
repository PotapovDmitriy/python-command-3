from sqlalchemy import Integer, String, Column, ForeignKeyConstraint

from database import Base


class Sneaker(Base):
    __tablename__ = 'sneakers'
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

    def __str__(self):
        return f"name: {self.name}; count: {self.count_products}; price: {self.price}"
