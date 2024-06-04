from api.v2.customer.models import Customer
from api.v2.customer.repositories import CustomerRepository
from api.v2.templates import CRUDService
from api.v2.customer.schemas import CustomerCreate, CustomerUpdate


class CustomerService(CRUDService[Customer, CustomerCreate, CustomerUpdate, CustomerRepository]):
    def __init__(self, customer_repository: CustomerRepository):
        super().__init__(customer_repository)


# with Session(engine) as session:
#     customer_repository = CustomerRepository(session)
#     customer_service = CustomerService(customer_repository)
#     customer = CustomerCreate(
#         first_name="John",
#         last_name="Doe",
#         email="john_doe@email.com",
#         phone="(702)-738-894-4861"
#     )
#     customer_repository.create(customer)

