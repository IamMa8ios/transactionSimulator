from uuid import UUID

from sqlalchemy.orm import Session, relationship

from api.v3.db import engine
from api.v3.enums import Availability
from api.v3.product.models import ProductVariant
from api.v3.product.schemas import ProductVariantCreate, ProductVariantRead, ProductVariantUpdate
from api.v3.templates import CRUDRepository

from api.v3.customer.models import Customer
from api.v3.shipment.models import BackorderShipment
from api.v3.customer_order.models import CustomerOrderItem


class ProductVariantRepository(CRUDRepository[ProductVariant, ProductVariantCreate, ProductVariantRead,
                               ProductVariantUpdate]):

    def __init__(self, db: Session):
        super().__init__(db, ProductVariant)


# with Session(engine) as session:
#     product_variant_repository = ProductVariantRepository(session)
#     product_variant = ProductVariantCreate(
#         product_id='e5494b20-7bfa-487b-b3f1-3ff87883e9d4',
#         color='Red',
#         pattern='Solid',
#         size='L',
#         image='images/products/47ff27df-93e4-4370-beda-77b9a34c4279/product-variant-2',
#         inventory=10,
#         availability=Availability.AVAILABLE_NOW,
#         price=100,
#         cost=50
#     )
#     product_variant_repository.create(product_variant)

# with Session(engine) as session:
#     product_variant_repository = ProductVariantRepository(session)
#     product_variant = ProductVariantUpdate(
#         product_id='e5494b20-7bfa-487b-b3f1-3ff87883e9d4',
#         color='Blue',
#         pattern='Solid',
#         size='L',
#         image='images/products/47ff27df-93e4-4370-beda-77b9a34c4279/product-variant-1',
#         inventory=10,
#         availability=Availability.AVAILABLE_NOW,
#         price=100,
#         cost=50
#     )
#     product_variant_repository.update(UUID('1e065f1c-c4c4-4ba6-9e1e-22f5c8f45acf'), product_variant)
