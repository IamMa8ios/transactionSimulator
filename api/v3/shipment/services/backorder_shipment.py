from api.v3.shipment.repositories import BackorderShipmentRepository
from api.v3.shipment.schemas import BackorderShipmentCreate, BackorderShipmentRead, BackorderShipmentUpdate
from api.v3.templates import CRUDService


class BackorderShipmentService(CRUDService[BackorderShipmentCreate, BackorderShipmentRead,
                               BackorderShipmentUpdate, BackorderShipmentRepository]):

    def __init__(self, backorder_shipment_repository: BackorderShipmentRepository):
        super().__init__(backorder_shipment_repository)
