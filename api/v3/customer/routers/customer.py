from fastapi import APIRouter

from api.v3.customer.dependencies import get_customer_service
from api.v3.customer.schemas import CustomerRead, CustomerCreate, CustomerUpdate
from api.v3.customer.services import CustomerService
from api.v3.templates import add_crud_routes

router = APIRouter(prefix="/api/v3/customer", tags=["Customer Management"])


add_crud_routes(router, CustomerService, CustomerCreate, CustomerRead, CustomerUpdate, get_customer_service)
