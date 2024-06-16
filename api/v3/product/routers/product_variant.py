from fastapi import APIRouter

from api.v3.product.dependencies import get_product_variant_service
from api.v3.product.schemas import ProductVariantRead, ProductVariantCreate, ProductVariantUpdate
from api.v3.product.services import ProductVariantService
from api.v3.templates.crud_router import add_crud_routes

router = APIRouter(prefix="/api/v3/product-variant", tags=["ProductVariant Variant Management"])

add_crud_routes(router, ProductVariantService, ProductVariantCreate, ProductVariantRead, ProductVariantUpdate,
                get_product_variant_service)
