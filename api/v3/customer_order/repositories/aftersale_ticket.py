from uuid import UUID

from sqlalchemy.orm import Session

from api.v3.db import engine
from api.v3.enums import TicketStatus
from api.v3.templates import CRUDRepository
from api.v3.customer_order.models import AftersaleTicket
from api.v3.customer_order.schemas import AftersaleTicketCreate, AftersaleTicketRead, AftersaleTicketUpdate

from api.v3.customer.models import Customer
from api.v3.shipment.models import CustomerOrderShipment
from api.v3.product.models import ProductVariant


class AftersaleTicketRepository(CRUDRepository[AftersaleTicket, AftersaleTicketCreate, AftersaleTicketRead,
                                AftersaleTicketUpdate]):

    def __init__(self, db: Session):
        super().__init__(db, AftersaleTicket)


# with Session(engine) as session:
#     ticket_repository = AftersaleTicketRepository(session)
#     item = AftersaleTicketCreate(
#         order_item_id=UUID('798ac783-401c-407c-a8e3-e6c4723ad9bd'),
#         details='Product Defective',
#         ticket_status=TicketStatus.OPEN
#     )
#     ticket_repository.create(item)
