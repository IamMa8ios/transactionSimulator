import uuid

from sqlalchemy import Column, UUID, ForeignKey, String, Date, func, Double, DateTime, CheckConstraint, Index
from sqlalchemy.orm import relationship

from api.v3.db import Base


class CustomerOrderShipment(Base):
    __tablename__ = 'customer_order_shipments'

    id = Column("order_shipment_id", UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4,
                nullable=False)
    order_id = Column(UUID(as_uuid=True), ForeignKey('customer_orders.order_id'), nullable=False)
    shipping_partner = Column(String(255), nullable=False)
    expected_at = Column(Date, default=func.current_date() + func.interval('1 day'), nullable=False)
    arrived_at = Column(Date)
    product_shipping_cost = Column(Double, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    customer_order = relationship("CustomerOrder", back_populates="customer_order_shipments")

    __table_args__ = (
        CheckConstraint('expected_at >= current_date', name='check_expected_at'),
        CheckConstraint('(arrived_at is null) or (arrived_at >= created_at)', name='check_arrived_at'),
        CheckConstraint('product_shipping_cost >= 0', name='check_product_shipping_cost'),
        CheckConstraint('updated_at >= created_at', name='check_updated_at'),
        Index('idx_shipments_order_id', 'order_id')
    )
