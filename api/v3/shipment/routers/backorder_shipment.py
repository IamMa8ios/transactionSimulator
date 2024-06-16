from fastapi import APIRouter

from api.v3.shipment.dependencies import get_backorder_shipment_service
from api.v3.shipment.schemas import BackorderShipmentRead, BackorderShipmentCreate, BackorderShipmentUpdate
from api.v3.shipment.services import BackorderShipmentService
from api.v3.templates.crud_router import add_crud_routes

router = APIRouter(prefix="/api/v3/backorder", tags=["Backorder Shipment Management"])

add_crud_routes(router, BackorderShipmentService, BackorderShipmentCreate, BackorderShipmentRead,
                BackorderShipmentUpdate, get_backorder_shipment_service)
