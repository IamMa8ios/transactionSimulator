from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status

from api.v3.customer.dependencies import get_customer_service
from api.v3.customer.schemas import CustomerRead, CustomerCreate, CustomerUpdate
from api.v3.customer.services import CustomerService

router = APIRouter(prefix="/api/v3/customer", tags=["Customer Management"])


@router.get("/all", response_model=List[CustomerRead])
async def get_all_customers(customer_service: Annotated[CustomerService, Depends(get_customer_service)]):
    return customer_service.get_all()


@router.get("/{customer_id}", response_model=CustomerRead)
async def get_customer(customer_id: UUID, customer_service: Annotated[CustomerService, Depends(get_customer_service)]):
    return customer_service.get_by_id(customer_id)


@router.get("/random", response_model=CustomerRead)
async def get_random_customer(customer_service: Annotated[CustomerService, Depends(get_customer_service)]):
    return customer_service.get_random()


@router.get("/email/{email}", response_model=CustomerRead)
async def get_customer_by_email(email: str, customer_service: Annotated[CustomerService,
                                Depends(get_customer_service)]):
    return customer_service.get_by_email(email=email)


@router.post("", response_model=CustomerRead, dependencies=[Depends(get_customer_service)],
             status_code=status.HTTP_201_CREATED)
async def create_customer(customer: CustomerCreate, customer_service: Annotated[CustomerService,
                          Depends(get_customer_service)]):
    return customer_service.create(customer)


@router.put("/{customer_id}", response_model=CustomerRead)
async def update_customer(customer_id: UUID, customer_data: CustomerUpdate,
                          customer_service: Annotated[CustomerService, Depends(get_customer_service)]):
    return customer_service.update(customer_id, customer_data)


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(customer_id: UUID, customer_service: Annotated[CustomerService,
                          Depends(get_customer_service)]):
    return customer_service.delete(customer_id)
