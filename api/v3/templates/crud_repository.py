from __future__ import annotations

import random
import uuid
from typing import TypeVar, Generic, Optional, List

from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.v3.db import Base

M = TypeVar('M', bound=Base)        # Model
C = TypeVar('C', bound=BaseModel)   # Model Create
R = TypeVar('R', bound=BaseModel)   # Model Read
U = TypeVar('U', bound=BaseModel)   # Model Update


class CRUDRepository(Generic[M, C, R, U]):

    def __init__(self, db: Session, model: M):
        self.model = model
        self.db = db

    def get_by_id(self, model_id: uuid.UUID) -> Optional[R]:
        return self.db.query(self.model).filter(self.model.id == model_id).first()

    def get_random(self) -> Optional[R]:
        return random.choice(self.db.query(self.model).all())

    def get_all(self) -> List[R]:
        return self.db.query(self.model).all()

    def get_multi(self, skip: int = 0, limit: int = 100) -> List[R]:
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def create(self, model_create: C) -> R:
        new_model_data = model_create.dict()
        db_model = self.model(**new_model_data)
        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)
        return db_model

    def create_multi(self, create_models: List[C]) -> List[R]:
        db_models = []
        for model_create in create_models:
            new_model_data = model_create.dict()
            db_models.append(self.model(**new_model_data))
        self.db.add_all(db_models)
        self.db.commit()
        self.db.refresh(db_models)
        return db_models

    def update(self, model_id: uuid.UUID, model_update: U) -> Optional[R]:
        db_model = self.get_by_id(model_id)
        print(db_model)
        if db_model:
            update_data = model_update.dict(exclude_unset=True)
            for field in update_data:
                setattr(db_model, field, update_data[field])
            self.db.commit()
            self.db.refresh(db_model)
        return db_model

    def delete(self, model_id: uuid.UUID) -> Optional[R]:
        model_in_db = self.db.query(self.model).get(model_id)
        if model_in_db:
            self.db.delete(model_in_db)
            self.db.commit()
        return model_in_db
