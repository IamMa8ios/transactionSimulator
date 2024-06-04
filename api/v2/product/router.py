from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter, Depends, status

from api.v2.product.dependencies import get_product_service
from api.v2.product.schemas.product import ProductRead, ProductCreate, ProductUpdate
from api.v2.product.services.product import ProductService

router = APIRouter(prefix="/api/v2/product", tags=["Product Management"])


@router.get("", response_model=List[ProductRead])
async def get_all_products(product_service: Annotated[ProductService, Depends(get_product_service)]):
    return product_service.get_all()


@router.get("/{product_id}", response_model=ProductRead)
async def get_product(product_id: UUID, product_service: Annotated[ProductService, Depends(get_product_service)]):
    return product_service.get_by_id(product_id)


@router.post("", response_model=ProductRead, dependencies=[Depends(get_product_service)],
             status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, product_service: Annotated[ProductService,
                         Depends(get_product_service)]):
    return product_service.create(product)


@router.put("/{product_id}", response_model=ProductRead)
async def update_product(product_id: UUID, product_data: ProductUpdate,
                         product_service: Annotated[ProductService, Depends(get_product_service)]):
    return product_service.update(product_id, product_data)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: UUID, product_service: Annotated[ProductService,
                         Depends(get_product_service)]):
    return product_service.delete(product_id)
