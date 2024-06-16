import random
from sqlalchemy.orm import Session

from api.v3.customer.repositories import CustomerRepository
from api.v3.customer_order.repositories import CustomerOrderItemRepository, AftersaleTicketRepository
from api.v3.customer_order.schemas import AftersaleTicketCreate
from api.v3.db import engine
from api.v3.enums import TicketStatus
from api.v3.product.repositories import ProductRepository, ProductVariantRepository
from api.v3.product.schemas import ProductCreate, ProductVariantCreate
from api.v3.product.models import Product, ProductVariant
from api.v3.shipment.models import CustomerOrderShipment, BackorderShipment
from api.v3.customer_order.models import CustomerOrder, CustomerOrderItem

details = [
    "Technical Support",
    "Product Defect or Damage",
    "Billing or Payment Issues",
    "Account Issues",
    "Feature Requests",
    "Installation or Setup Assistance",
    "Performance Issues",
    "Product Returns or Exchanges",
    "Warranty Claims",
    "General Inquiries"
]


def generate_aftersale_ticket_data(num_tickets):
    with Session(engine) as session:
        aftersale_repository = AftersaleTicketRepository(session)

        for _ in range(num_tickets):
            item_id = CustomerOrderItemRepository(session).get_random().id
            ticket_details = random.choice(details)
            status = random.choice(list(TicketStatus))

            ticket = AftersaleTicketCreate(
                order_item_id=item_id,
                details=ticket_details,
                ticket_status=status
            )

            aftersale_repository.create(ticket)


# generate_aftersale_ticket_data(10)
