from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None


class ProductCreate(ProductBase):
    title: str


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(ProductBase):
    id: int
    title: str

    class Config:
        orm_mode = True


class Product(ProductBase):
    pass


class ProductInDb(ProductInDBBase):
    pass


