import uuid

from sqlalchemy import Column, UUID, ForeignKey, Enum, String, Integer, Float, TIMESTAMP, func
from sqlalchemy.orm import relationship

from api.v2.db import Base
from api.v2.transaction.transaction_enums import PaymentMethod, OrderStatus


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(
        "transaction_id",
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
        nullable=False
    )
    customer_id = Column("customer_id", UUID(as_uuid=True),
                         ForeignKey("customers.customer_id"), nullable=False)
    product_id = Column("product_id", UUID(as_uuid=True),
                        ForeignKey("products.product_id"), nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    channel_lvl1 = Column(String, nullable=False)
    channel_lvl2 = Column(String, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    revenue = Column(Float, default=0, nullable=False)
    shipping_id = Column(String, default="N/A", nullable=False)
    order_status = Column(Enum(OrderStatus), default=OrderStatus.received, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), server_onupdate=func.now(), nullable=False)

    product = relationship("Product", backref='transactions', secondary='transactions')
    customer = relationship("Customer", backref='transactions', secondary='transactions')
