import uuid

from sqlalchemy import Column, UUID, ForeignKey, String, Integer, Date, func, Float, DateTime, CheckConstraint, Index
from sqlalchemy.orm import relationship

from api.v3.db import Base


class BackorderShipment(Base):
    __tablename__ = 'backorder_shipments'

    id = Column("backorder_shipment_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True,
                nullable=False)
    variant_id = Column(UUID(as_uuid=True), ForeignKey('product_variants.variant_id'), nullable=False)
    supplier = Column(String(255), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    expected_at = Column(Date, default=func.current_date() + func.interval('1 day'), nullable=False)
    arrived_at = Column(Date)
    backorder_shipping_cost = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=func.current_timestamp(), nullable=False)

    variant = relationship("ProductVariant", back_populates="backorder_shipments")

    __table_args__ = (
        CheckConstraint('quantity > 0', name='quantity_positive'),
        CheckConstraint('expected_at >= current_date', name='expected_at_valid'),
        CheckConstraint('(arrived_at is null) or (arrived_at >= created_at)', name='arrived_at_valid'),
        CheckConstraint('backorder_shipping_cost >= 0', name='backorder_shipping_cost_positive'),
        CheckConstraint('updated_at >= created_at', name='check_updated_at'),
        Index('idx_supply_shipments_variant_id', 'variant_id')
    )
