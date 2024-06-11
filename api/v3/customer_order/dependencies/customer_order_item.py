from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v2.db import get_db
from api.v3.customer_order.repositories import CustomerOrderItemRepository
from api.v3.customer_order.services import CustomerOrderItemService


def get_customer_order_item_service(session: Annotated[Session, Depends(get_db)]) -> CustomerOrderItemService:
    customer_order_item_repository = CustomerOrderItemRepository(db=session)
    return CustomerOrderItemService(customer_order_item_repository=customer_order_item_repository)
