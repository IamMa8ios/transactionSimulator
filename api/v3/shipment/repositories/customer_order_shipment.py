from datetime import date
from uuid import UUID

from sqlalchemy.orm import Session, relationship

from api.v3.db import engine
from api.v3.shipment.models import CustomerOrderShipment
from api.v3.shipment.schemas import CustomerOrderShipmentUpdate, CustomerOrderShipmentRead, CustomerOrderShipmentCreate
from api.v3.templates import CRUDRepository
from api.v3.customer_order.models import CustomerOrder

from api.v3.product.models import ProductVariant
from api.v3.customer.models import Customer


class CustomerOrderShipmentRepository(CRUDRepository[CustomerOrderShipment, CustomerOrderShipmentCreate, CustomerOrderShipmentRead,
                                      CustomerOrderShipmentUpdate]):
    def __init__(self, db: Session):
        super().__init__(db, CustomerOrderShipment)


# with Session(engine) as session:
#     backorder_repository = CustomerOrderShipmentRepository(session)
#     backorder = ProductShipmentCreate(
#         order_id=UUID('58a063f4-cf5f-4bb1-89a1-2536d6f5e987'),
#         shipping_partner='Shipping Partner 1',
#         expected_at=date.today(),
#         arrived_at=None,
#         product_shipping_cost=5
#     )
#     backorder_repository.create(backorder)
