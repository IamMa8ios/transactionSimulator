from sqlalchemy.orm import Session

from api.v2.product.models import Product
from api.v2.product.schemas import ProductCreate, ProductUpdate
from api.v2.templates import CRUDRepository


class ProductRepository(CRUDRepository[Product, ProductCreate, ProductUpdate]):

    def __init__(self, db: Session):
        super().__init__(db, Product)


# with Session(engine) as session:
#     product_repository = ProductRepository(session)
#     product = ProductCreate(
#         type=ProductType.a,
#         category=ProductCategory.top,
#         subcategory=ProductSubcategory.coat,
#         inventory=10,
#         price=50.0,
#         cost=25.0
#     )
#     product_repository.create(product)
