from api.v3.customer.repositories import CustomerRepository
from api.v3.customer.schemas import CustomerCreate, CustomerUpdate, CustomerRead
from api.v3.templates import CRUDService


class CustomerService(CRUDService[CustomerCreate, CustomerRead, CustomerUpdate, CustomerRepository]):
    def __init__(self, customer_repository: CustomerRepository):
        super().__init__(customer_repository)

    def get_by_email(self, email: str) -> CustomerRead:
        return self.get_by_email(email)
