from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v3.db import get_db
from api.v3.product.repositories import ProductVariantRepository
from api.v3.product.services import ProductVariantService


def get_product_variant_service(session: Annotated[Session, Depends(get_db)]) -> ProductVariantService:
    product_variant_repository = ProductVariantRepository(session)
    return ProductVariantService(product_variant_repository=product_variant_repository)
