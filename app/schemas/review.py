from typing import Optional

from pydantic import BaseModel


class ReviewBase(BaseModel):
    text: Optional[str] = None
    rating: Optional[int] = None
    user_id: Optional[id] = None


class ReviewCreate(ReviewBase):
    pass


class ReviewInDBBase(ReviewBase):
    id: int
    review_product_id: int
    approved: bool

    class Config:
        orm_mode = True


class Review(ReviewBase):
    pass


class ReviewInDb(ReviewInDBBase):
    pass


