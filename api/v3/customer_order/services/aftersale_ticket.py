from api.v3.customer_order.repositories import AftersaleTicketRepository
from api.v3.customer_order.schemas import AftersaleTicketCreate, AftersaleTicketUpdate, AftersaleTicketRead
from api.v3.templates import CRUDService


class AftersaleTicketService(CRUDService[AftersaleTicketCreate, AftersaleTicketRead,
                             AftersaleTicketUpdate, AftersaleTicketRepository]):

    def __init__(self, aftersale_ticket_repository: AftersaleTicketRepository):
        super().__init__(aftersale_ticket_repository)
