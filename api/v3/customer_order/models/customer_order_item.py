import uuid

from sqlalchemy import Column, UUID, ForeignKey, Integer, DateTime, func, CheckConstraint, Index, UniqueConstraint
from sqlalchemy.orm import relationship

from api.v3.db import Base


class CustomerOrderItem(Base):
    __tablename__ = 'customer_order_items'

    id = Column("order_item_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                unique=True, nullable=False)
    order_id = Column(UUID(as_uuid=True), ForeignKey('customer_orders.order_id'), nullable=False)
    variant_id = Column(UUID(as_uuid=True), ForeignKey('product_variants.variant_id'), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=func.current_timestamp(), nullable=False)

    customer_order = relationship("CustomerOrder", back_populates="customer_order_items")
    variant = relationship("ProductVariant", back_populates="customer_order_items")
    aftersale_tickets = relationship("AftersaleTicket", back_populates="customer_order_item")

    __table_args__ = (
        CheckConstraint('quantity > 0', name='check_quantity'),
        CheckConstraint('updated_at >= created_at', name='check_updated_at'),
        UniqueConstraint('order_id', 'variant_id', name='order_id_variant_id_uc'),
        Index('idx_customer_order_items_order_id', 'order_id'),
        Index('idx_customer_order_items_variant_id', 'variant_id')
    )
