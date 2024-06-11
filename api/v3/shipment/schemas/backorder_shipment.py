from datetime import date, datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, confloat


class BackorderShipmentBase(BaseModel):
    variant_id: UUID
    supplier: str = Field(max_length=255)
    quantity: confloat(gt=0)
    expected_at: date = Field(default_factory=lambda: date.today())
    arrived_at: Optional[date]
    backorder_shipping_cost: confloat(ge=0)
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class BackorderShipmentCreate(BackorderShipmentBase):
    pass


class BackorderShipmentUpdate(BackorderShipmentBase):
    updated_at: datetime = datetime.now()


class BackorderShipmentRead(BackorderShipmentBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
