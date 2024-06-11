from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v3.db import get_db
from api.v3.shipment.repositories import BackorderShipmentRepository
from api.v3.shipment.services import BackorderShipmentService


def get_backorder_shipment_service(session: Annotated[Session, Depends(get_db)]) -> BackorderShipmentService:
    backorder_shipment_repository = BackorderShipmentRepository(session)
    return BackorderShipmentService(backorder_shipment_repository=backorder_shipment_repository)
