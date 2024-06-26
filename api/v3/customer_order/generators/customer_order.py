import random
from sqlalchemy.orm import Session

from api.v3.customer.repositories import CustomerRepository
from api.v3.customer_order.repositories import CustomerOrderRepository
from api.v3.customer_order.schemas import CustomerOrderCreate
from api.v3.db import engine
from api.v3.enums import Availability, ChannelLevel1, ChannelLevel2, PaymentMethod, OrderStatus, channel_mapping
from api.v3.product.repositories import ProductRepository, ProductVariantRepository
from api.v3.product.schemas import ProductCreate, ProductVariantCreate
from api.v3.product.models import Product, ProductVariant
from api.v3.shipment.models import CustomerOrderShipment, BackorderShipment
from api.v3.customer_order.models import CustomerOrder, CustomerOrderItem


def generate_customer_order_data(num_orders):
    with Session(engine) as session:
        order_repository = CustomerOrderRepository(session)

        for _ in range(num_orders):
            customer_id = CustomerRepository(session).get_random().id
            channel_lvl1 = random.choice(list(ChannelLevel1))
            channel_lvl2 = random.choice(channel_mapping[channel_lvl1])
            payment_method = random.choice(list(PaymentMethod))
            order_status = random.choice(list(OrderStatus))

            order = CustomerOrderCreate(
                customer_id=customer_id,
                channel_lvl1=channel_lvl1,
                channel_lvl2=channel_lvl2,
                payment_method=payment_method,
                order_status=order_status
            )

            order_repository.create(order)


# generate_customer_order_data(10)
