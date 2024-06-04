from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel, constr, EmailStr

from api.v2.transaction.schemas.transaction import TransactionRead


class CustomerBase(BaseModel):
    first_name: constr(max_length=50)
    last_name: constr(max_length=50)
    email: EmailStr
    phone: constr(max_length=18)


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    updated_at: datetime = datetime.now()


class CustomerRead(CustomerBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    transactions: List[TransactionRead] = []

    class Config:
        orm_mode = True
