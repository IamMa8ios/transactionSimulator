from fastapi import APIRouter

from api.v3.customer_order.dependencies import get_customer_order_service
from api.v3.customer_order.schemas import CustomerOrderRead, CustomerOrderCreate, CustomerOrderUpdate
from api.v3.customer_order.services import CustomerOrderService
from api.v3.templates.crud_router import add_crud_routes

router = APIRouter(prefix="/api/v3/order", tags=["Customer Order Management"])

add_crud_routes(router, CustomerOrderService, CustomerOrderCreate, CustomerOrderRead, CustomerOrderUpdate,
                get_customer_order_service)
