from datetime import date
from uuid import UUID

from sqlalchemy.orm import Session, relationship

from api.v3.db import engine
from api.v3.product.models import ProductVariant
from api.v3.shipment.models import BackorderShipment
from api.v3.shipment.schemas import BackorderShipmentUpdate, BackorderShipmentRead, BackorderShipmentCreate
from api.v3.templates import CRUDRepository

from api.v3.customer_order.models import CustomerOrderItem
from api.v3.customer.models import Customer


class BackorderShipmentRepository(CRUDRepository[BackorderShipment, BackorderShipmentCreate, BackorderShipmentRead,
                                  BackorderShipmentUpdate]):
    def __init__(self, db: Session):
        super().__init__(db, BackorderShipment)


# with Session(engine) as session:
#     backorder_repository = BackorderShipmentRepository(session)
#     backorder = BackorderShipmentCreate(
#         variant_id=UUID('1e065f1c-c4c4-4ba6-9e1e-22f5c8f45acf'),
#         supplier='Supplier 1',
#         quantity=100,
#         expected_at=date.today(),
#         arrived_at=None,
#         backorder_shipping_cost=15
#     )
#     backorder_repository.create(backorder)
