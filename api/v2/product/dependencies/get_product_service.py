from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v2.product.repositories import ProductRepository
from api.v2.product.services import ProductService
from api.v2.db import get_db


def get_product_service(session: Annotated[Session, Depends(get_db)]) -> ProductService:
    product_repository = ProductRepository(db=session)
    return ProductService(product_repository=product_repository)
