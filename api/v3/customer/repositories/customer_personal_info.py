import uuid
from datetime import date
from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Session

from api.v3.customer.models import CustomerPersonalInfo
from api.v3.customer.schemas import CustomerPersonalInfoCreate, CustomerPersonalInfoRead, CustomerPersonalInfoUpdate
from api.v3.db import engine
from api.v3.templates import CRUDRepository


from api.v3.customer.models import Customer
from api.v3.customer_order.models import CustomerOrder
from api.v3.shipment.models import CustomerOrderShipment
from api.v3.product.models import ProductVariant


class CustomerPersonalInfoRepository(CRUDRepository[CustomerPersonalInfo, CustomerPersonalInfoCreate,
                                     CustomerPersonalInfoRead, CustomerPersonalInfoUpdate]):

    def __init__(self, db: Session):
        super().__init__(db, CustomerPersonalInfo)

    def get_by_customer_id(self, customer_id: uuid.UUID) -> Optional[CustomerPersonalInfoRead]:
        return self.model.query.filter(CustomerPersonalInfo.customer_id == customer_id).first()


# with Session(engine) as session:
#     info_repository = CustomerPersonalInfoRepository(session)
#     info = CustomerPersonalInfoCreate(
#         customer_id='491df5b3-200c-4e5b-a6b4-521ea448938a',
#         date_of_birth=date(2000, 1, 1)
#     )
#     info_repository.create(info)

# with Session(engine) as session:
#     info_repository = CustomerPersonalInfoRepository(session)
#     info = CustomerPersonalInfoUpdate(
#         customer_id='491df5b3-200c-4e5b-a6b4-521ea448938a',
#         international_customer=False,
#         street_address='Home 1'
#     )
#     info_repository.update(UUID('28fcc890-4b1d-4904-b58c-d6fdf1b8c7d6'), info)
