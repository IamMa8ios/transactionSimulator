import uuid
from typing import TypeVar, Generic, Optional

from pydantic import BaseModel

from api.v3.templates import CRUDRepository

C = TypeVar('C', bound=BaseModel)   # Model Create
R = TypeVar('R', bound=BaseModel)   # Model Read
U = TypeVar('U', bound=BaseModel)   # Model Update
X = TypeVar("X", bound=CRUDRepository)  # Model Repository


class CRUDService(Generic[C, R, U, X]):

    def __init__(self, model_repository: X):
        self.model_repository = model_repository

    def get_all(self) -> list[R]: return self.model_repository.get_all()

    def get_by_id(self, model_id: uuid.UUID) -> Optional[R]: return self.model_repository.get_by_id(model_id)

    def get_random(self) -> Optional[R]:
        return self.model_repository.get_random()

    def get_multi(self, skip: int = 0, limit: int = 100) -> list[R]:
        return self.model_repository.get_multi(skip, limit)

    def create(self, model_create: C) -> R: return self.model_repository.create(model_create)

    def update(self, model_id: uuid.UUID, model_update: U) -> R:
        return self.model_repository.update(model_id, model_update)

    def delete(self, model_id: uuid.UUID) -> None: return self.model_repository.delete(model_id)
