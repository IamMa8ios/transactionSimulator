from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v3.customer.repositories import CustomerPersonalInfoRepository
from api.v3.customer.services import CustomerPersonalInfoService
from api.v3.db import get_db


def get_customer_personal_info_service(session: Annotated[Session, Depends(get_db)]) -> CustomerPersonalInfoService:
    customer_info_repository = CustomerPersonalInfoRepository(db=session)
    return CustomerPersonalInfoService(customer_info_repository=customer_info_repository)
