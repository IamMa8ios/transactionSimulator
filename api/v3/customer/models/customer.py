import uuid

from sqlalchemy import Column, UUID, String, func, DateTime, CheckConstraint, Index
from sqlalchemy.orm import relationship

from api.v3.db import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column("customer_id", UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(18), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    personal_info = relationship("CustomerPersonalInfo", uselist=False, back_populates="customer")
    customer_orders = relationship("CustomerOrder", back_populates="customer")

    __table_args__ = (
        CheckConstraint('updated_at >= created_at', name='check_updated_at'),
        Index('idx_customers_email', 'email'),
        Index('idx_customers_phone', 'phone')
    )
