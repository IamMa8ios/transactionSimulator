from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v3.customer_order.repositories import AftersaleTicketRepository
from api.v3.customer_order.services import AftersaleTicketService
from api.v3.db import get_db


def get_aftersale_ticket_service(session: Annotated[Session, Depends(get_db)]) -> AftersaleTicketService:
    aftersale_ticket_repository = AftersaleTicketRepository(session)
    return AftersaleTicketService(aftersale_ticket_repository=aftersale_ticket_repository)
