from typing import Annotated, TypeVar, Type

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v3.db import get_db
from api.v3.templates import CRUDService, CRUDRepository

R = TypeVar("R", bound=CRUDRepository)
S = TypeVar("S", bound=CRUDService)


def get_service(session: Annotated[Session, Depends(get_db)], repository_cls: Type[R], service_cls: Type[S]) -> S:
    repository = repository_cls(db=session)
    return service_cls(repository)
