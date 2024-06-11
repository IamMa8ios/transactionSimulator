import uuid

from sqlalchemy import Column, UUID, ForeignKey, Date, String, Boolean, Double, DateTime, func, CheckConstraint, Index
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.orm import relationship

from api.v3.db import Base


class CustomerPersonalInfo(Base):
    __tablename__ = 'customer_personal_info'

    id = Column("customer_info_id", UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4,
                nullable=False)
    customer_id = Column(UUID(as_uuid=True), ForeignKey('customers.customer_id'), unique=True, nullable=False)
    date_of_birth = Column(Date)
    gender = Column(String(10), default='N/A')
    international_customer = Column(Boolean)
    street_address = Column(String(100))
    ipv4_address = Column(INET)
    job_title = Column(String(255))
    zip_code = Column(String(15))
    city = Column(String(50))
    state = Column(String(50))
    county = Column(String(50))
    country = Column(String(50))
    median_household_income = Column(Double)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    customer = relationship("Customer", back_populates="personal_info")

    __table_args__ = (
        CheckConstraint('updated_at >= created_at', name='check_updated_at'),
        CheckConstraint('median_household_income > 0', name='check_median_household_income'),
        Index('idx_customer_personal_info_customer_id', 'customer_id')
    )
