from __future__ import annotations
import uuid
from typing import TypeVar, Generic, Optional, List

from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.v2.db import Base

T = TypeVar('T', bound=Base)        # Model
U = TypeVar('U', bound=BaseModel)   # Model Create
V = TypeVar('V', bound=BaseModel)   # Model Update


class CRUDRepository(Generic[T, U, V]):

    def __init__(self, db: Session, model: T):
        self.model = model
        self.db = db

    def get_by_id(self, model_id: uuid.UUID) -> Optional[T]:
        return self.db.query(self.model).filter(self.model.customer_id == model_id).first()

    def get_all(self) -> List[T]:
        return self.db.query(self.model).all()

    def get_multi(self, skip: int = 0, limit: int = 100) -> List[T]:
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def create(self, model_create: U) -> T:
        new_model_data = model_create.dict()
        db_model = self.model(**new_model_data)
        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)
        return db_model

    def update(self, model_id: uuid.UUID, model_update: V) -> Optional[T]:
        db_model = self.get_by_id(model_id)
        if db_model:
            update_data = model_update.dict(exclude_unset=True)
            for field in update_data:
                setattr(db_model, field, update_data[field])
            self.db.commit()
            self.db.refresh(db_model)
        return db_model

    def delete(self, model_id: uuid.UUID) -> Optional[T]:
        model_in_db = self.db.query(self.model).get(model_id)
        if model_in_db:
            self.db.delete(model_in_db)
            self.db.commit()
        return model_in_db
