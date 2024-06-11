from api.v3.customer_order.models import CustomerOrderItem
from api.v3.customer_order.repositories import CustomerOrderItemRepository
from api.v3.customer_order.schemas import CustomerOrderItemCreate, CustomerOrderItemUpdate, CustomerOrderItemRead
from api.v3.templates import CRUDService


class CustomerOrderItemService(CRUDService[CustomerOrderItem, CustomerOrderItemCreate, CustomerOrderItemRead,
                               CustomerOrderItemUpdate, CustomerOrderItemRepository]):

    def __init__(self, customer_order_item_repository: CustomerOrderItemRepository):
        super().__init__(customer_order_item_repository)
