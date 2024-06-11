from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v3.customer.repositories import CustomerRepository
from api.v3.customer.services import CustomerService
from api.v3.db import get_db


def get_customer_service(session: Annotated[Session, Depends(get_db)]) -> CustomerService:
    customer_repository = CustomerRepository(db=session)
    return CustomerService(customer_repository=customer_repository)
