from fastapi import APIRouter

from api.v3.shipment.dependencies import get_customer_order_shipment_service
from api.v3.shipment.schemas import CustomerOrderShipmentRead, CustomerOrderShipmentCreate, CustomerOrderShipmentUpdate
from api.v3.shipment.services import CustomerOrderShipmentService
from api.v3.templates.crud_router import add_crud_routes

router = APIRouter(prefix="/api/v3/shipment", tags=["Customer Order Shipment Management"])

add_crud_routes(router, CustomerOrderShipmentService, CustomerOrderShipmentCreate, CustomerOrderShipmentRead,
                CustomerOrderShipmentUpdate, get_customer_order_shipment_service)
