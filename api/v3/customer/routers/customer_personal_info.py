from fastapi import APIRouter, Depends, status

from api.v3.customer.dependencies import get_customer_personal_info_service
from api.v3.customer.schemas import CustomerPersonalInfoCreate, CustomerPersonalInfoRead, CustomerPersonalInfoUpdate
from api.v3.customer.services import CustomerPersonalInfoService
from api.v3.templates import add_crud_routes

router = APIRouter(prefix="/api/v3/personal_info", tags=["Customer's Personal Info Management"])


add_crud_routes(router, CustomerPersonalInfoService, CustomerPersonalInfoCreate, CustomerPersonalInfoRead,
                CustomerPersonalInfoUpdate, get_customer_personal_info_service)
