import random
from sqlalchemy.orm import Session

from api.v3.db import engine
from api.v3.enums import Availability
from api.v3.product.repositories import ProductRepository, ProductVariantRepository
from api.v3.product.schemas import ProductCreate, ProductVariantCreate
from api.v3.product.models import Product, ProductVariant
from api.v3.shipment.models import CustomerOrderShipment, BackorderShipment
from api.v3.customer_order.models import CustomerOrder, CustomerOrderItem

colors = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Pink", "Purple", "Orange", "Gray"]
patterns = ["Solid", "Striped", "Plaid", "Polka Dot", "Chevron", "Paisley", "Floral", "Geometric"]
sizes = ["XS", "S", "M", "L", "XL", "XXL"]


def generate_product_variants(num_variants):
    with Session(engine) as session:
        variant_repository = ProductVariantRepository(session)
        product = ProductRepository(session).get_random()
        for num in range(num_variants):
            color = random.choice(colors)
            pattern = random.choice(patterns)
            size = random.choice(sizes)
            image = f"api/v3/products/{product.id}/variants/{num}"
            inventory = random.randint(1, 100)
            availability = random.choice(list(Availability))
            price = round(random.uniform(5.0, 1000.0), 2)
            cost = round(price * random.uniform(0.5, 0.8), 2)

            variant = ProductVariantCreate(
                product_id=product.id,
                color=color,
                pattern=pattern,
                size=size,
                image=image,
                inventory=inventory,
                availability=availability,
                price=price,
                cost=cost
            )

            variant_repository.create(variant)


generate_product_variants(10)
