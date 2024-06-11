import uuid

from sqlalchemy import Column, UUID, ForeignKey, DateTime, func, CheckConstraint, Index, String
from sqlalchemy.orm import relationship

from api.v3.db import Base
from api.v3.enums import PaymentMethod, OrderStatus, StringEnum


class CustomerOrder(Base):
    __tablename__ = 'customer_orders'

    id = Column("order_id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    customer_id = Column(UUID(as_uuid=True), ForeignKey('customers.customer_id'), nullable=False)
    channel_lvl1 = Column(String(255), nullable=False)
    channel_lvl2 = Column(String(255), nullable=False)
    payment_method = Column(StringEnum(PaymentMethod), nullable=False)
    order_status = Column(StringEnum(OrderStatus), default=OrderStatus.RECEIVED, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    customer = relationship("Customer", back_populates="customer_orders")
    customer_order_items = relationship("CustomerOrderItem", back_populates="customer_order")
    customer_order_shipments = relationship("CustomerOrderShipment", back_populates="customer_order")

    __table_args__ = (
        CheckConstraint(
            "payment_method in ('Cash', 'Cash On Delivery', 'Credit Card', 'Debit Card', 'Bank Transfer', "
            "'Autopay', 'Reward Points', 'Buy Now Pay Later', 'Cheque', 'Mobile Wallet')",
            name='check_payment_method'),
        CheckConstraint("order_status in ('Received', 'Processing', 'Shipped', 'Cancelled', 'Completed', 'Refunded')",
                        name='check_order_status'),
        CheckConstraint('updated_at >= created_at', name='check_updated_at'),
        Index('idx_customer_orders_customer_id', 'customer_id')
    )
