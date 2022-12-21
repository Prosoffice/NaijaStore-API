from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Review(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    rating = Column(Integer)
    review_product_id = Column(Integer)
    user_id = Column(Integer)
    approved = Column(Boolean(), default=False)
    product = relationship("ReviewProduct", back_populates="reviews")
    comments = relationship("Comments", back_populates="review")




