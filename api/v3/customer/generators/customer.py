import csv
import uuid

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from api.v3.customer.models import CustomerPersonalInfo
from api.v3.customer.schemas import CustomerCreate
from api.v3.customer_order.models import CustomerOrder
from api.v3.db import engine
from api.v3.shipment.models import CustomerOrderShipment
from api.v3.product.models import ProductVariant

from api.v3.customer.repositories import CustomerRepository

with open('../../data/customer.csv') as customer_data:
    reader = csv.reader(customer_data)
    header = next(reader)
    with Session(engine) as session:
        customer_repository = CustomerRepository(session)
        for row in reader:
            customer = CustomerCreate(
                first_name=row[0],
                last_name=row[1],
                email=row[2],
                phone=row[3]
            )
            try:
                customer_repository.create(customer)
                session.commit()
            except IntegrityError as e:
                print(f"IntegrityError: {e}")
                session.rollback()
