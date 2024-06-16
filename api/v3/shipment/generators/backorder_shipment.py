import random
from datetime import date, timedelta

from sqlalchemy.orm import Session

from api.v3.db import engine
from api.v3.product.repositories import ProductVariantRepository
from api.v3.shipment.repositories import BackorderShipmentRepository
from api.v3.shipment.schemas import BackorderShipmentCreate

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


def generate_backorder_shipment_data(num_orders):
    with Session(engine) as session:
        backorder_repository = BackorderShipmentRepository(session)

        for _ in range(num_orders):
            variant_id = ProductVariantRepository(session).get_random().id
            supplier = random.choice(shipping_companies)
            quantity = random.randint(10, 50)
            random_days = random.randint(1, 5)
            expected_at = date.today() + timedelta(days=random_days)
            random_days = random.randint(1, 5)
            arrived_at = date.today() + timedelta(days=random_days)
            backorder_shipping_cost = round(random.uniform(5.0, 50.0), 2)

            shipment = BackorderShipmentCreate(
                variant_id=variant_id,
                supplier=supplier,
                quantity=quantity,
                expected_at=expected_at,
                arrived_at=arrived_at,
                backorder_shipping_cost=backorder_shipping_cost
            )

            backorder_repository.create(shipment)


# generate_backorder_shipment_data(10)
