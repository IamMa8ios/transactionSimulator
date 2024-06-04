from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v2.db import get_db
from api.v2.transaction.repositories import TransactionRepository
from api.v2.transaction.services.transaction import TransactionService


def get_transaction_service(session: Annotated[Session, Depends(get_db)]) -> TransactionService:
    transaction_repository = TransactionRepository(db=session)
    return TransactionService(transaction_repository=transaction_repository)
