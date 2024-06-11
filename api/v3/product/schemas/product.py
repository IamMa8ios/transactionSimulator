from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    title: str = Field(max_length=255)
    brand: str = Field(max_length=255)
    description: str = Field(default='', max_length=255)
    type: str = Field(max_length=255)
    category: str = Field(max_length=255)
    subcategory: str = Field(max_length=255)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    updated_at: datetime = datetime.now()


class ProductRead(ProductBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
