from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, computed_field

from api.v2.product.product_enums import ProductType, ProductCategory, ProductSubcategory
from api.v2.transaction.schemas.transaction import TransactionRead


class ProductBase(BaseModel):
    type: ProductType
    category: ProductCategory
    subcategory: ProductSubcategory
    inventory: int = 0
    price: float
    cost: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    transactions: List[TransactionRead] = []

    @computed_field
    @property
    def profit(self) -> float:
        return self.price - self.cost

    class Config:
        orm_mode = True
