import uuid

from sqlalchemy import Column, UUID, ForeignKey, String, DateTime, func, CheckConstraint, Index
from sqlalchemy.orm import relationship

from api.v3.db import Base
from api.v3.enums import StringEnum, TicketStatus


class AftersaleTicket(Base):
    __tablename__ = 'aftersale_tickets'

    id = Column("aftersale_ticket_id", UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4,
                nullable=False)
    order_item_id = Column(UUID(as_uuid=True), ForeignKey('customer_order_items.order_item_id'), nullable=False)
    details = Column(String(255), nullable=False)
    ticket_status = Column(StringEnum(TicketStatus), default=TicketStatus.OPEN, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    customer_order_item = relationship("CustomerOrderItem", back_populates="aftersale_tickets")

    __table_args__ = (
        CheckConstraint("support_status in ('Open', 'Processing', 'Resolved', 'Unresolved')", name='check_status'),
        CheckConstraint('updated_at >= created_at', name='check_updated_at'),
        Index('idx_aftersale_support_order_item_id', 'order_item_id')
    )
