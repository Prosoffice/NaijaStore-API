from typing import Optional

from pydantic import BaseModel


class CommentBase(BaseModel):
    text: Optional[str] = None


class CommentCreate(CommentBase):
    pass


class CommentInDBBase(CommentBase):
    id: int
    user_id: int
    review_id: int
    approved: bool

    class Config:
        orm_mode = True


class Comment(CommentBase):
    pass


class CommentInDb(CommentInDBBase):
    pass


