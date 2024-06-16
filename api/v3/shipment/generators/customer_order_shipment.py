import random
from datetime import date, timedelta

from sqlalchemy.orm import Session

from api.v3.customer_order.repositories import CustomerOrderRepository
from api.v3.db import engine
from api.v3.shipment.repositories import CustomerOrderShipmentRepository
from api.v3.shipment.schemas import CustomerOrderShipmentCreate

shipping_companies = [
    "ParcelToThePeople",
    "ShipHappens",
    "ExpresslyYours",
    "BoxToTheFuture",
    "FleetStreet",
    "DeliverEase",
    "SendInTheClowns",
    "ShipShape",
    "SpeedyGonzales",
    "Mailstrom"
]


def generate_customer_order_shipment_data(num_orders):
    with Session(engine) as session:
        shipment_repository = CustomerOrderShipmentRepository(session)

        for _ in range(num_orders):
            order_id = CustomerOrderRepository(session).get_random().id
            shipping_partner = random.choice(shipping_companies)
            random_days = random.randint(1, 5)
            expected_at = date.today() + timedelta(days=random_days)
            random_days = random.randint(1, 5)
            arrived_at = date.today() + timedelta(days=random_days)
            product_shipping_cost = round(random.uniform(5.0, 50.0), 2)

            shipment = CustomerOrderShipmentCreate(
                order_id=order_id,
                shipping_partner=shipping_partner,
                expected_at=expected_at,
                arrived_at=arrived_at,
                product_shipping_cost=product_shipping_cost
            )

            shipment_repository.create(shipment)


# generate_customer_order_shipment_data(10)
