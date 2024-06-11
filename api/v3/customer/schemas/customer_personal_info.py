from pydantic import BaseModel, Field, field_validator, PastDate
from datetime import datetime, date
from uuid import UUID
from typing import Optional


class CustomerPersonalInfoBase(BaseModel):
    customer_id: UUID
    date_of_birth: Optional[PastDate] = None
    gender: Optional[str] = Field(max_length=10, default='N/A')
    international_customer: Optional[bool] = None
    street_address: Optional[str] = Field(None, max_length=100)
    ipv4_address: Optional[str] = Field(None, max_length=15)
    job_title: Optional[str] = Field(None, max_length=255)
    zip_code: Optional[str] = Field(None, max_length=15)
    city: Optional[str] = Field(None, max_length=50)
    state: Optional[str] = Field(None, max_length=50)
    county: Optional[str] = Field(None, max_length=50)
    country: Optional[str] = Field(None, max_length=50)
    median_household_income: Optional[float] = Field(None, gt=0)


class CustomerPersonalInfoCreate(CustomerPersonalInfoBase):
    pass


class CustomerPersonalInfoUpdate(CustomerPersonalInfoBase):
    updated_at: datetime = datetime.now()


class CustomerPersonalInfoRead(CustomerPersonalInfoBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
