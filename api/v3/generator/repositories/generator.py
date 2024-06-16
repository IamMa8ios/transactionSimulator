import csv
import random
from datetime import date, timedelta

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

# Models
from api.v3.customer.models import Customer, CustomerPersonalInfo
from api.v3.product.models import Product, ProductVariant
from api.v3.customer_order.models import CustomerOrder, CustomerOrderItem, AftersaleTicket
from api.v3.shipment.models import CustomerOrderShipment, BackorderShipment

# Schemas
from api.v3.customer.schemas import CustomerCreate, CustomerPersonalInfoCreate
from api.v3.product.schemas import ProductCreate, ProductVariantCreate 
from api.v3.customer_order.schemas import CustomerOrderCreate, CustomerOrderItemCreate, AftersaleTicketCreate
from api.v3.shipment.schemas import CustomerOrderShipmentCreate, BackorderShipmentCreate

# Repositories
from api.v3.customer.repositories import CustomerRepository, CustomerPersonalInfoRepository
from api.v3.product.repositories import ProductRepository, ProductVariantRepository
from api.v3.customer_order.repositories import (CustomerOrderRepository, CustomerOrderItemRepository, 
                                                AftersaleTicketRepository)
from api.v3.shipment.repositories import CustomerOrderShipmentRepository, BackorderShipmentRepository

# Data Structures
from api.v3.enums import Availability, ChannelLevel1, channel_mapping, PaymentMethod, OrderStatus, TicketStatus
from api.v3.product.generators.product import types, brand_mapping, brands, categories, subcategories
from api.v3.product.generators.product_variant import colors, patterns, sizes
from api.v3.customer_order.generators.aftersale_ticket import details
from api.v3.shipment.generators.customer_order_shipment import shipping_companies


class GeneratorRepository:
    
    def __init__(self, db: Session):
        self.db = db
        
    def generate_customers(self):
        with open('api/v3/data/customer.csv') as customer_data:
            reader = csv.reader(customer_data)
            next(reader)

            customer_repository = CustomerRepository(self.db)

            for row in reader:
                customer = CustomerCreate(
                    first_name=row[0],
                    last_name=row[1],
                    email=row[2],
                    phone=row[3]
                )
                try:
                    customer_repository.create(customer)
                    self.db.commit()
                except IntegrityError:
                    self.db.rollback()
                # except IntegrityError as e:
                    # print(f"IntegrityError: {e}")

    def generate_customer_personal_info(self):

        with open('api/v3/data/customer_personal_info.csv', encoding="utf8") as customer_personal_data:
            reader = csv.reader(customer_personal_data)
            next(reader)

            customers = CustomerRepository(self.db).get_all()

            if customers.__sizeof__() > 0:

                customer_repository = CustomerPersonalInfoRepository(self.db)

                for row, customer in zip(reader, customers):
                    customer_info = CustomerPersonalInfoCreate(
                        customer_id=customer.id,
                        date_of_birth=row[0],
                        international_customer=row[8] != 'Greece',
                        street_address=row[2],
                        ipv4_address=row[3],
                        job_title=row[4],
                        zip_code=row[5],
                        city=row[6],
                        state=row[7],
                        country=row[8],
                        median_household_income=round(random.uniform(24000.00, 250000.99), 2)
                    )
                    try:
                        customer_repository.create(customer_info)
                        self.db.commit()
                    except IntegrityError:
                        self.db.rollback()
                    # except IntegrityError as e:
                    #   print(f"IntegrityError: {e}")
            else:
                print("No customers found")
                
    def generate_products(self, number_of_products: int = 10):

        product_repository = ProductRepository(self.db)
        total = 0
        while total < number_of_products:
            product_type = random.choice(types)
            brand = random.choice(brand_mapping.get(product_type, brands))
            category = random.choice(categories)
            subcategory = random.choice(subcategories.get(category, ["General"]))
            title = f"{product_type} in {subcategory} product by {brand}"
            description = (f"This {product_type} product by {brand} is perfect for anyone looking to enhance their "
                           f"experience with top-quality {product_type.lower()} items.")
            price = round(random.uniform(5.0, 1000.0), 2)
            cost = round(price * random.uniform(0.5, 0.8), 2)

            product = ProductCreate(
                type=product_type,
                title=title,
                brand=brand,
                description=description,
                category=category,
                subcategory=subcategory,
                price=price,
                cost=cost
            )

            try:
                product_repository.create(product)
                total += 1
            except IntegrityError:
                self.db.rollback()

    def generate_product_variants(self, number_of_products: int = 1, number_of_variants: int = 3):
        
        variant_repository = ProductVariantRepository(self.db)
        product = ProductRepository(self.db).get_random()

        for _ in range(number_of_products):
            total = 1
            while total <= number_of_variants:
                color = random.choice(colors)
                pattern = random.choice(patterns)
                size = random.choice(sizes)
                image = f"api/v3/products/{product.id}/variants/{total}"
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
    
                try:
                    variant_repository.create(variant)
                    total += 1
                except IntegrityError:
                    self.db.rollback()
                    
    def generate_customer_orders(self, number_of_orders: int = 3):

        order_repository = CustomerOrderRepository(self.db)

        for _ in range(number_of_orders):
            customer_id = CustomerRepository(self.db).get_random().id
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

            try:
                order_repository.create(order)
            except IntegrityError:
                self.db.rollback()
                
    def generate_customer_order_items(self, number_of_orders: int = 1, number_of_items: int = 3):

        item_repository = CustomerOrderItemRepository(self.db)
        order_id = CustomerOrderRepository(self.db).get_random().id

        for _ in range(number_of_orders):
            for __ in range(number_of_items):

                variant_id = ProductVariantRepository(self.db).get_random().id
                quantity = random.randint(1, 10)

                item = CustomerOrderItemCreate(
                    order_id=order_id,
                    variant_id=variant_id,
                    quantity=quantity
                )

                try:
                    item_repository.create(item)
                except IntegrityError:
                    self.db.rollback()

    def generate_aftersale_tickets(self, number_of_tickets: int = 1):
        
        aftersale_repository = AftersaleTicketRepository(self.db)

        for _ in range(number_of_tickets):
            item_id = CustomerOrderItemRepository(self.db).get_random().id
            ticket_details = random.choice(details)
            status = random.choice(list(TicketStatus))

            ticket = AftersaleTicketCreate(
                order_item_id=item_id,
                details=ticket_details,
                ticket_status=status
            )
            
            try:
                aftersale_repository.create(ticket)
            except IntegrityError:
                self.db.rollback()
                
    def generate_customer_order_shipments(self, number_of_shipments: int = 1):
        
        shipment_repository = CustomerOrderShipmentRepository(self.db)

        for _ in range(number_of_shipments):
            order_id = CustomerOrderRepository(self.db).get_random().id
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

            try:
                shipment_repository.create(shipment)
            except IntegrityError:
                self.db.rollback()
                
    def generate_backorder_shipments(self, number_of_shipments: int = 1):

        backorder_repository = BackorderShipmentRepository(self.db)

        for _ in range(number_of_shipments):
            variant_id = ProductVariantRepository(self.db).get_random().id
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

            try:
                backorder_repository.create(shipment)
            except IntegrityError:
                self.db.rollback()
