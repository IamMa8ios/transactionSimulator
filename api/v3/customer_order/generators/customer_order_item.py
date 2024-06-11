import random
from sqlalchemy.orm import Session

from api.v3.customer_order.repositories import CustomerOrderRepository, CustomerOrderItemRepository
from api.v3.customer_order.schemas import CustomerOrderCreate, CustomerOrderItemCreate
from api.v3.db import engine
from api.v3.enums import Availability, ChannelLevel1, ChannelLevel2, PaymentMethod, OrderStatus
from api.v3.product.repositories import ProductRepository, ProductVariantRepository
from api.v3.product.schemas import ProductCreate, ProductVariantCreate
from api.v3.product.models import Product, ProductVariant
from api.v3.shipment.models import CustomerOrderShipment, BackorderShipment
from api.v3.customer_order.models import CustomerOrder, CustomerOrderItem


def generate_customer_order_data(orders, num_order_items):
    with Session(engine) as session:
        item_repository = CustomerOrderItemRepository(session)
        order_id = CustomerOrderRepository(session).get_random().id

        for i in range(orders):
            for j in range(num_order_items):

                variant_id = ProductVariantRepository(session).get_random().id
                quantity = random.randint(1, 10)

                item = CustomerOrderItemCreate(
                    order_id=order_id,
                    variant_id=variant_id,
                    quantity=quantity
                )

                item_repository.create(item)


generate_customer_order_data(3, 5)
