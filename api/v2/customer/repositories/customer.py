from sqlalchemy.orm import Session

from api.v2.customer.models import Customer
from api.v2.customer.schemas import CustomerCreate, CustomerUpdate
from api.v2.templates import CRUDRepository


class CustomerRepository(CRUDRepository[Customer, CustomerCreate, CustomerUpdate]):

    def __init__(self, db: Session) -> None:
        super().__init__(db, Customer)


# with Session(engine) as session:
#     customer_repository = CustomerRepository(session)
#     customer = CustomerCreate(
#         first_name="John",
#         last_name="Doe",
#         email="john_doe@email.com",
#         phone="(702)-738-894-4861"
#     )
#     customer_repository.create(customer)
