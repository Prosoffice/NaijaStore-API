
from sqlalchemy import Column, Integer, String, Boolean, Float
from app.db.base_class import Base


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Integer, index=True)
    price = Column(Float, nullable=False)
    