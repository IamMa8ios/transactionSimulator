from typing import List, Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status

from api.v3.customer.dependencies import get_customer_personal_info_service
from api.v3.customer.schemas import CustomerPersonalInfoCreate, CustomerPersonalInfoRead, CustomerPersonalInfoUpdate
from api.v3.customer.services import CustomerPersonalInfoService

router = APIRouter(prefix="/api/v3/personal_info", tags=["Customer's Personal Info Management"])


@router.get("/all", response_model=List[CustomerPersonalInfoRead])
async def get_all_customer_personal_info(customer_personal_info_service: Annotated[CustomerPersonalInfoService, 
                                         Depends(get_customer_personal_info_service)]):
    return customer_personal_info_service.get_all()


@router.get("/{customer_personal_info_id}", response_model=CustomerPersonalInfoRead)
async def get_customer(customer_personal_info_id: UUID, customer_personal_info_service:
                       Annotated[CustomerPersonalInfoService, Depends(get_customer_personal_info_service)]):
    return customer_personal_info_service.get_by_id(customer_personal_info_id)


@router.get("/customer/{customer_id}", response_model=CustomerPersonalInfoRead)
async def get_by_customer_id(customer_id: UUID, customer_personal_info_service: Annotated[CustomerPersonalInfoService,
                             Depends(get_customer_personal_info_service)]):
    return customer_personal_info_service.get_by_customer_id(customer_id)


@router.get("/random", response_model=CustomerPersonalInfoRead)
async def get_random_customer(customer_personal_info_service: Annotated[CustomerPersonalInfoService,
                              Depends(get_customer_personal_info_service)]):
    return customer_personal_info_service.get_random()


@router.post("", response_model=CustomerPersonalInfoRead,
             dependencies=[Depends(get_customer_personal_info_service)], status_code=status.HTTP_201_CREATED)
async def create_customer_personal_info(customer_personal_info: CustomerPersonalInfoCreate,
                                        customer_personal_info_service: Annotated[CustomerPersonalInfoService, Depends(
                                            get_customer_personal_info_service)]):
    return customer_personal_info_service.create(customer_personal_info)


@router.put("/{customer_personal_info_id}", response_model=CustomerPersonalInfoRead)
async def update_customer_personal_info(customer_personal_info_id: UUID, customer_data: CustomerPersonalInfoUpdate,
                                        customer_personal_info_service: Annotated[
                                            CustomerPersonalInfoService, Depends(get_customer_personal_info_service)]):
    return customer_personal_info_service.update(customer_personal_info_id, customer_data)


@router.delete("/{customer_personal_info_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer_personal_info(customer_personal_info_id: UUID, customer_personal_info_service: Annotated[
                                        CustomerPersonalInfoService, Depends(get_customer_personal_info_service)]):
    return customer_personal_info_service.delete(customer_personal_info_id)
