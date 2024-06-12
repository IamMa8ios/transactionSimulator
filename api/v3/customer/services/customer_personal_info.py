import uuid
from typing import Optional

from api.v3.customer.repositories import CustomerPersonalInfoRepository
from api.v3.customer.schemas import CustomerPersonalInfoCreate, CustomerPersonalInfoUpdate, CustomerPersonalInfoRead
from api.v3.templates import CRUDService


class CustomerPersonalInfoService(CRUDService[CustomerPersonalInfoCreate,
                                  CustomerPersonalInfoRead, CustomerPersonalInfoUpdate, CustomerPersonalInfoRepository]
                                  ):
    def __init__(self, customer_info_repository: CustomerPersonalInfoRepository):
        super().__init__(customer_info_repository)

    def get_by_customer_id(self, customer_id: uuid.UUID) -> Optional[CustomerPersonalInfoRead]:
        return self.model_repository.get_by_customer_id(customer_id=customer_id)
