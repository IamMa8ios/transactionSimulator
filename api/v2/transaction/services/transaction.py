from api.v2.templates import CRUDService
from api.v2.transaction.models import Transaction
from api.v2.transaction.repositories import TransactionRepository
from api.v2.transaction.schemas import TransactionCreate, TransactionUpdate


class TransactionService(CRUDService[Transaction, TransactionCreate, TransactionUpdate, TransactionRepository]):

    def __init__(self, transaction_repository: TransactionRepository):
        super().__init__(transaction_repository)
