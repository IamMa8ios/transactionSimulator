from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v3.db import get_db
from api.v3.shipment.repositories import CustomerOrderShipmentRepository
from api.v3.shipment.services import CustomerOrderShipmentService


def get_customer_order_shipment_service(session: Annotated[Session, Depends(get_db)]) -> CustomerOrderShipmentService:
    customer_order_shipment_repository = CustomerOrderShipmentRepository(session)
    return CustomerOrderShipmentService(customer_order_shipment_repository=customer_order_shipment_repository)
