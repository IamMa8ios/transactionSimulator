import csv
import random

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from api.v3.customer.models import CustomerPersonalInfo
from api.v3.customer.schemas import CustomerPersonalInfoCreate
from api.v3.customer_order.models import CustomerOrder
from api.v3.db import engine
from api.v3.shipment.models import CustomerOrderShipment
from api.v3.product.models import ProductVariant
from api.v3.customer.repositories import CustomerRepository
from api.v3.customer.models import Customer

from api.v3.customer.repositories import CustomerPersonalInfoRepository


def generate_customer_personal_info():

    with open('../../data/customer_personal_info.csv', encoding="utf8") as customer_personal_data:
        reader = csv.reader(customer_personal_data)
        next(reader)
        with Session(engine) as session:
            customers = CustomerRepository(session).get_all()
            print(customers.__sizeof__())
            customer_repository = CustomerPersonalInfoRepository(session)
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
                    session.commit()
                except IntegrityError as e:
                    print(f"IntegrityError: {e}")
                    session.rollback()


# generate_customer_personal_info()
