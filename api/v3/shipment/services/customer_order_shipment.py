from api.v3.shipment.repositories import CustomerOrderShipmentRepository
from api.v3.shipment.schemas import CustomerOrderShipmentCreate, CustomerOrderShipmentRead, CustomerOrderShipmentUpdate
from api.v3.templates import CRUDService


class CustomerOrderShipmentService(CRUDService[CustomerOrderShipmentCreate,
                                   CustomerOrderShipmentRead, CustomerOrderShipmentUpdate,
                                   CustomerOrderShipmentRepository]):

    def __init__(self, customer_order_shipment_repository: CustomerOrderShipmentRepository):
        super().__init__(customer_order_shipment_repository)
