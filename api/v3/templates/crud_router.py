from typing import Type, TypeVar, List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status
from pydantic import BaseModel

from api.v3.templates import CRUDRepository, CRUDService

T = TypeVar("T", bound=BaseModel)
R = TypeVar("R", bound=CRUDRepository)
S = TypeVar("S", bound=CRUDService)


def add_crud_routes(router: APIRouter, service_cls: Type[S], model_create, model_read, model_update, get_service):

    @router.get("/all", response_model=List[model_read])
    async def get_all(service: Annotated[service_cls, Depends(get_service)]):
        return service.get_all()

    @router.get("/{item_id}", response_model=model_read)
    async def get_by_id(item_id: UUID, service: Annotated[service_cls, Depends(get_service)]):
        return service.get_by_id(item_id)

    @router.get("/random", response_model=model_read)
    async def get_random(service: Annotated[service_cls, Depends(get_service)]):
        return service.get_random()

    @router.post("", response_model=model_read, status_code=status.HTTP_201_CREATED)
    async def create(item: model_create, service: Annotated[service_cls, Depends(get_service)]):
        return service.create(item)

    @router.put("/{item_id}", response_model=model_read)
    async def update(item_id: UUID, item_data: model_update, service: Annotated[service_cls, Depends(get_service)]):
        return service.update(item_id, item_data)

    @router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete(item_id: UUID, service: Annotated[service_cls, Depends(get_service)]):
        return service.delete(item_id)
