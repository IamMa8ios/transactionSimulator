from fastapi import APIRouter

from api.v3.customer_order.dependencies import get_customer_order_item_service
from api.v3.customer_order.schemas import CustomerOrderItemRead, CustomerOrderItemCreate, CustomerOrderItemUpdate
from api.v3.customer_order.services import CustomerOrderItemService
from api.v3.templates.crud_router import add_crud_routes

router = APIRouter(prefix="/api/v3/order-item", tags=["Customer Order Item Management"])

add_crud_routes(router, CustomerOrderItemService, CustomerOrderItemCreate, CustomerOrderItemRead,
                CustomerOrderItemUpdate, get_customer_order_item_service)
