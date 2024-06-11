from datetime import date, datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, confloat


class CustomerOrderShipmentBase(BaseModel):
    order_id: UUID
    shipping_partner: str = Field(max_length=255)
    expected_at: date = Field(default_factory=lambda: date.today())
    arrived_at: Optional[date]
    product_shipping_cost: confloat(ge=0)
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class CustomerOrderShipmentCreate(CustomerOrderShipmentBase):
    pass


class CustomerOrderShipmentUpdate(CustomerOrderShipmentBase):
    updated_at: datetime = datetime.now()


class CustomerOrderShipmentRead(CustomerOrderShipmentBase):
    shipment_id: UUID
    transaction_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
