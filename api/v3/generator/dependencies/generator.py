from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from api.v3.db import get_db
from api.v3.generator.repositories import GeneratorRepository
from api.v3.generator.services import GeneratorService


def get_generator_service(session: Annotated[Session, Depends(get_db)]) -> GeneratorService:
    generator_repository = GeneratorRepository(db=session)
    return GeneratorService(generator_repository=generator_repository)
