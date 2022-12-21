
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class ReviewProduct(Base):
    __tablename__ = "review_product"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Integer, index=True)
    type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    photo_url = Column(String, nullable=False)
    reviews = relationship("Review", back_populates="product")



    