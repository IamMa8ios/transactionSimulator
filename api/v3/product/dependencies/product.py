from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v3.db import get_db
from api.v3.product.repositories import ProductRepository
from api.v3.product.services import ProductService
from api.v3.templates import get_service


def get_product_service(session: Annotated[Session, Depends(get_db)]) -> ProductService:
    return get_service(session, ProductRepository, ProductService)
