from uuid import UUID

from sqlalchemy.orm import Session

from api.v3.db import engine
from api.v3.templates import CRUDRepository
from api.v3.customer_order.models import CustomerOrderItem
from api.v3.customer_order.schemas import CustomerOrderItemCreate, CustomerOrderItemRead, CustomerOrderItemUpdate

from api.v3.customer.models import Customer
from api.v3.product.models import ProductVariant
from api.v3.shipment.models import CustomerOrderShipment


class CustomerOrderItemRepository(CRUDRepository[CustomerOrderItem, CustomerOrderItemCreate, CustomerOrderItemRead,
                                  CustomerOrderItemUpdate]):

    def __init__(self, db: Session):
        super().__init__(db, CustomerOrderItem)


# with Session(engine) as session:
#     item_repository = CustomerOrderItemRepository(session)
#     item = CustomerOrderItemCreate(
#         order_id=UUID('58a063f4-cf5f-4bb1-89a1-2536d6f5e987'),
#         variant_id=UUID('b01e2614-0c38-4394-afeb-954ed405dab5'),
#         quantity=1
#     )
#     item_repository.create(item)
