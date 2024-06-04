from typing import Annotated, List
from uuid import UUID

from fastapi import Depends, APIRouter
from starlette import status

from api.v2.transaction.dependencies import get_transaction_service
from api.v2.transaction.schemas import TransactionRead, TransactionCreate, TransactionUpdate
from api.v2.transaction.services.transaction import TransactionService

router = APIRouter(prefix="/api/v2/transaction", tags=["Transaction Management"])


@router.get("", response_model=List[TransactionRead])
async def get_all_transactions(transaction_service: Annotated[TransactionService, Depends(get_transaction_service)]):
    return transaction_service.get_all()


@router.get("/{transaction_id}", response_model=TransactionRead)
async def get_transaction(transaction_id: UUID, transaction_service: Annotated[TransactionService,
                          Depends(get_transaction_service)]):
    return transaction_service.get_by_id(transaction_id)


@router.post("", response_model=TransactionRead, dependencies=[Depends(get_transaction_service)],
             status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction: TransactionCreate, transaction_service: Annotated[TransactionService,
                             Depends(get_transaction_service)]):
    return transaction_service.create(transaction)


@router.put("/{transaction_id}", response_model=TransactionRead)
async def update_transaction(transaction_id: UUID, transaction_data: TransactionUpdate,
                             transaction_service: Annotated[TransactionService, Depends(get_transaction_service)]):
    return transaction_service.update(transaction_id, transaction_data)


@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transaction(transaction_id: UUID, transaction_service: Annotated[TransactionService,
                             Depends(get_transaction_service)]):
    return transaction_service.delete(transaction_id)
