from api.v3.customer.models import Customer
from api.v3.customer.repositories import CustomerRepository
from api.v3.customer.schemas import CustomerCreate, CustomerUpdate, CustomerRead
from api.v3.templates import CRUDService


class CustomerService(CRUDService[Customer, CustomerCreate, CustomerRead, CustomerUpdate, CustomerRepository]):
    def __init__(self, customer_repository: CustomerRepository):
        super().__init__(customer_repository)

    def get_by_email(self, email: str) -> Customer:
        return self.get_by_email(email)
