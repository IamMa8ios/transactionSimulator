from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v2.db import get_db
from api.v3.customer_order.repositories import CustomerOrderRepository
from api.v3.customer_order.services import CustomerOrderService


def get_customer_order_service(session: Annotated[Session, Depends(get_db)]) -> CustomerOrderService:
    customer_order_repository = CustomerOrderRepository(db=session)
    return CustomerOrderService(customer_order_repository=customer_order_repository)
