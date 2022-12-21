from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Review(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    rating = Column(Integer)
    user_id = Column(Integer)
    approved = Column(Boolean(), default=False)
    review_product_id = Column(Integer, ForeignKey("review_product.id"))
    product = relationship("ReviewProduct", back_populates="reviews")
    comments = relationship("Comment", back_populates="review")




