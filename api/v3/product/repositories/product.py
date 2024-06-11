from sqlalchemy.orm import Session

from api.v3.db import engine
from api.v3.product.models import Product
from api.v3.product.schemas import ProductCreate, ProductRead, ProductUpdate
from api.v3.templates import CRUDRepository

from api.v3.customer.models import Customer
from api.v3.customer_order.models import CustomerOrderItem
from api.v3.shipment.models import BackorderShipment


class ProductRepository(CRUDRepository[Product, ProductCreate, ProductRead, ProductUpdate]):

    def __init__(self, db: Session):
        super().__init__(db, Product)


# with Session(engine) as session:
#     product_repository = ProductRepository(session)
#     product = ProductCreate(
#         type="A",
#         title='Product Of Type A',
#         brand='Brand 1',
#         description='Product Of Type A, Category 1 And SubCategory 1',
#         category='Category 1',
#         subcategory='Subcategory 1'
#     )
#     product_repository.create(product)
