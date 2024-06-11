from sqlalchemy.orm import Session

from api.v3.customer.models import Customer
from api.v3.customer.schemas import CustomerCreate, CustomerRead, CustomerUpdate
from api.v3.db import engine
from api.v3.templates import CRUDRepository

# Needed for testing
# from api.v3.customer.models import CustomerPersonalInfo
# from api.v3.customer_order.models import CustomerOrder
# from api.v3.shipment.models import CustomerOrderShipment
# from api.v3.product.models import ProductVariant


class CustomerRepository(CRUDRepository[Customer, CustomerCreate, CustomerRead, CustomerUpdate]):

    def __init__(self, db: Session):
        super().__init__(db, Customer)

    def get_by_email(self, email: str):
        return self.db.query(Customer.email == email).first()

# with Session(engine) as session:
#     customer_repository = CustomerRepository(session)
#     customer = CustomerCreate(
#         first_name="John",
#         last_name="Doe",
#         email="john_doe@email.com",
#         phone="(702)-738-894-4861"
#     )
#     customer_repository.create(customer)
