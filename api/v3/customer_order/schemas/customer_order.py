from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, computed_field, Field

from api.v3.enums import PaymentMethod, OrderStatus
from api.v3.customer_order.schemas.customer_order_item import CustomerOrderItemRead


class CustomerOrderBase(BaseModel):
    customer_id: UUID
    payment_method: PaymentMethod
    channel_lvl1: str = Field(max_length=255)
    channel_lvl2: str = Field(max_length=255)
    order_status: OrderStatus = OrderStatus.RECEIVED


class CustomerOrderCreate(CustomerOrderBase):
    pass


class CustomerOrderUpdate(CustomerOrderBase):
    updated_at: datetime = datetime.now()


class CustomerOrderRead(CustomerOrderBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    # items: List[TransactionItemRead] = []

    # @computed_field
    # @property
    # def revenue(self) -> float:
    #     revenue = 0.0
    #     for item in self.items:
    #         revenue += item.revenue
    #     return revenue

    class Config:
        orm_mode = True
