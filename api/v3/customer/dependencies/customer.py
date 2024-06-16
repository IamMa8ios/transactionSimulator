from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v3.customer.repositories import CustomerRepository
from api.v3.customer.services import CustomerService
from api.v3.db import get_db
from api.v3.templates import get_service


def get_customer_service(session: Annotated[Session, Depends(get_db)]) -> CustomerService:
    return get_service(session, CustomerRepository, CustomerService)
