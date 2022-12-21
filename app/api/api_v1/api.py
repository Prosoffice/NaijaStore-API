from fastapi import APIRouter

from app.api.api_v1.endpoints import login, review_products

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(review_products, tags=["reviewProducts"])