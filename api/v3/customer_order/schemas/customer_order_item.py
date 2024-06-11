from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field, computed_field


class CustomerOrderItemBase(BaseModel):
    order_id: UUID
    variant_id: UUID
    quantity: int = Field(default=1, gt=0)


class CustomerOrderItemCreate(CustomerOrderItemBase):
    pass


class CustomerOrderItemUpdate(CustomerOrderItemBase):
    updated_at: datetime = datetime.now()


class CustomerOrderItemRead(CustomerOrderItemBase):
    id: UUID
    order_id: UUID
    variation_id: UUID
    created_at: datetime
    updated_at: datetime

    @computed_field
    @property
    def revenue(self) -> float:
        return self.quantity*self.price

    class Config:
        orm_mode = True
