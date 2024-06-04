from sqlalchemy.orm import Session

from api.v2.db import engine
from api.v2.templates import CRUDRepository
from api.v2.transaction.models import Transaction
from api.v2.transaction.schemas import TransactionCreate, TransactionUpdate
from api.v2.transaction.transaction_enums import PaymentMethod, OrderStatus


class TransactionRepository(CRUDRepository[Transaction, TransactionCreate, TransactionUpdate]):

    def __init__(self, db: Session):
        super().__init__(db, Transaction)


# with Session(engine) as session:
#     transaction_repository = TransactionRepository(session)
#     transaction = TransactionCreate(
#         customer_id="4e344ae2-727f-4c4d-b01b-67ac75611500",
#         product_id="04a6d18f-f0d7-4423-8f6f-3f9c4e2cd7ec",
#         payment_method=PaymentMethod.cash,
#         channel_lvl1="Marketplace",
#         channel_lvl2="EBay",
#         quantity=10,
#         revenue=500.0,
#         shipping_id="PLACEHOLDER",
#         order_status=OrderStatus.received
#     )
#     transaction_repository.create(transaction)
