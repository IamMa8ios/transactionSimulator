from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from api.v2.transaction.transaction_enums import PaymentMethod, OrderStatus


class TransactionBase(BaseModel):
    customer_id: UUID
    product_id: UUID
    payment_method: PaymentMethod
    channel_lvl1: str
    channel_lvl2: str
    quantity: int
    revenue: float
    shipping_id: str
    order_status: OrderStatus


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    updated_at: datetime = datetime.now()


class TransactionRead(TransactionBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
