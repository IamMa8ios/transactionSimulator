from api.v3.customer_order.models import CustomerOrder
from api.v3.customer_order.repositories import CustomerOrderRepository
from api.v3.customer_order.schemas import CustomerOrderCreate, CustomerOrderRead, CustomerOrderUpdate
from api.v3.templates import CRUDService


class CustomerOrderService(CRUDService[CustomerOrder, CustomerOrderCreate, CustomerOrderRead, CustomerOrderUpdate,
                           CustomerOrderRepository]):

    def __init__(self, customer_order_repository: CustomerOrderRepository):
        super().__init__(customer_order_repository)
