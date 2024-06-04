import uuid
from typing import TypeVar, Generic

T = TypeVar("T")  # Model
U = TypeVar("U")  # Model Create
V = TypeVar("V")  # Model Update
X = TypeVar("X")  # Model Repository


class CRUDService(Generic[T, U, V, X]):

    def __init__(self, model_repository: X):
        self.model_repository = model_repository

    def get_all(self) -> list[T]: return self.model_repository.get_all()

    def get_by_id(self, model_id: uuid.UUID) -> T: return self.model_repository.get_by_id(model_id)

    def create(self, model_create: U) -> T: return self.model_repository.create(model_create)

    def update(self, model_id: uuid.UUID, model_update: V) -> T:
        return self.model_repository.update(model_id, model_update)

    def delete(self, model_id: uuid.UUID) -> None: return self.model_repository.delete(model_id)