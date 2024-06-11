from sqlalchemy.orm import Session

from api.v3.db import engine
from api.v3.templates import CRUDRepository
from api.v3.customer_order.models import CustomerOrder
from api.v3.customer_order.schemas import CustomerOrderCreate, CustomerOrderRead, CustomerOrderUpdate

from api.v3.customer.models import Customer
from api.v3.shipment.models import CustomerOrderShipment
from api.v3.product.models import ProductVariant


class CustomerOrderRepository(CRUDRepository[CustomerOrder, CustomerOrderCreate, CustomerOrderRead,
                              CustomerOrderUpdate]):

    def __init__(self, db: Session):
        super().__init__(db, CustomerOrder)


# with Session(engine) as session:
#     order_repository = CustomerOrderRepository(session)
#     order = CustomerOrderCreate(
#         customer_id='491df5b3-200c-4e5b-a6b4-521ea448938a',
#         channel_lvl1='Marketplace',
#         channel_lvl2='Amazon',
#         payment_method='Debit Card',
#         order_status='Received'
#     )
#     order_repository.create(order)

