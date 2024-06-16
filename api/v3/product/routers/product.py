from fastapi import APIRouter

from api.v3.product.dependencies import get_product_service
from api.v3.product.schemas import ProductRead, ProductCreate, ProductUpdate
from api.v3.product.services import ProductService
from api.v3.templates.crud_router import add_crud_routes

router = APIRouter(prefix="/api/v3/product", tags=["Product Management"])

add_crud_routes(router, ProductService, ProductCreate, ProductRead, ProductUpdate, get_product_service)
