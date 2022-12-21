from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, models, crud
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/accommodations", response_model=List[schemas.User])
def read_review_products(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    review_products = crud.review_product.get_all_by_type(db, type="Accommodation")
    return review_products


@router.get("/events", response_model=List[schemas.User])
def read_review_products(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    review_products = crud.review_product.get_all_by_type(db, type="Event")
    return review_products


@router.get("/Restaurants", response_model=List[schemas.User])
def read_review_products(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    review_products = crud.review_product.get_all_by_type(db, type="Restaurant")
    return review_products