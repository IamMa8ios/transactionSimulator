from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class CustomerBase(BaseModel):
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    phone: str = Field(min_length=15, max_length=17)


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    updated_at: datetime = datetime.now()


class CustomerRead(CustomerBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
