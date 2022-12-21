from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Comment(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    approved = Column(Boolean(), default=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    review_id = Column(Integer, ForeignKey("review.id"))
    review = relationship("Review", back_populates="comments")

