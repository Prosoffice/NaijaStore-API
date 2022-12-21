from typing import Optional

from pydantic import BaseModel


class ReviewProductBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None
    photo_url: Optional[str] = None
    type: Optional[str] = None


class ReviewProductCreate(ReviewProductBase):
    title: str


class ReviewProductUpdate(ReviewProductBase):
    pass


class ReviewProductInDBBase(ReviewProductBase):
    id: int
    title: str

    class Config:
        orm_mode = True


class ReviewProduct(ReviewProductInDBBase):
    pass


class ReviewProductInDb(ReviewProductInDBBase):
    pass


