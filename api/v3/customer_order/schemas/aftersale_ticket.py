from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from api.v3.enums import TicketStatus


class AftersaleTicketBase(BaseModel):
    order_item_id: UUID
    details: str = Field(max_length=255)
    ticket_status: TicketStatus = Field(default=TicketStatus.OPEN)


class AftersaleTicketCreate(AftersaleTicketBase):
    order_item_id: UUID


class AftersaleTicketUpdate(AftersaleTicketBase):
    updated_at: datetime = datetime.now()


class AftersaleTicketRead(AftersaleTicketBase):
    id: UUID
    transaction_item_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
