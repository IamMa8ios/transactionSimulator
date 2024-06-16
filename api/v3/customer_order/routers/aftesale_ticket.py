from fastapi import APIRouter

from api.v3.customer_order.dependencies import get_aftersale_ticket_service
from api.v3.customer_order.schemas import AftersaleTicketRead, AftersaleTicketCreate, AftersaleTicketUpdate
from api.v3.customer_order.services import AftersaleTicketService
from api.v3.templates.crud_router import add_crud_routes

router = APIRouter(prefix="/api/v3/aftersale", tags=["Aftersale Management"])

add_crud_routes(router, AftersaleTicketService, AftersaleTicketCreate, AftersaleTicketRead, AftersaleTicketUpdate,
                get_aftersale_ticket_service)
