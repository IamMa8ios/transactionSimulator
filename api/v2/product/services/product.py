from sqlalchemy.orm import Session

from api.v2.db import engine
from api.v2.product.models import Product
from api.v2.product.product_enums import ProductType, ProductCategory, ProductSubcategory
from api.v2.product.repositories import ProductRepository
from api.v2.product.schemas import ProductCreate, ProductUpdate
from api.v2.templates import CRUDService


class ProductService(CRUDService[Product, ProductCreate, ProductUpdate, ProductRepository]):

    def __init__(self, product_repository: ProductRepository):
        super().__init__(product_repository)


# with Session(engine) as session:
#     product_repository = ProductRepository(session)
#     product_service = ProductService(product_repository)
#     product = ProductCreate(
#         type=ProductType.a,
#         category=ProductCategory.top,
#         subcategory=ProductSubcategory.coat,
#         inventory=10,
#         price=50.0,
#         cost=25.0
#     )
#     product_repository.create(product)
