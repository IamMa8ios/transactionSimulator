from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field, computed_field

from api.v3.enums import Availability


class ProductVariantBase(BaseModel):
    product_id: UUID
    color: str = Field(max_length=255)
    pattern: str = Field(max_length=255, default='Solid')
    size: str = Field(max_length=5)
    image: str = Field(max_length=255)
    inventory: int = Field(default=0, ge=0)
    availability: Availability = Availability.AVAILABLE_NOW
    price: float = Field(gt=0)
    cost: float = Field(gt=0)


class ProductVariantCreate(ProductVariantBase):
    pass


class ProductVariantUpdate(ProductVariantBase):
    updated_at: datetime = datetime.now()


class ProductVariantRead(ProductVariantBase):
    variation_id: UUID
    created_at: datetime
    updated_at: datetime

    @computed_field
    @property
    def profit(self) -> float:
        return self.price - self.cost

    class Config:
        orm_mode = True
