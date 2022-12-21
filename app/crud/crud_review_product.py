from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.review_product import ReviewProduct
from app.schemas.review_product import ReviewProductCreate, ReviewProductUpdate


class CRUDProduct(CRUDBase[ReviewProduct, ReviewProductCreate, ReviewProductUpdate]):

    def get_all_by_type(self, db: Session, *, type: str) -> Optional[ReviewProduct]:
        return db.query(ReviewProduct).filter(ReviewProduct.type == type).all()


review_product = CRUDProduct(ReviewProduct)