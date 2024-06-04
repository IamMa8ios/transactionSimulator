import uuid

from sqlalchemy import Column, UUID, String, TIMESTAMP, func
from sqlalchemy.orm import relationship

from api.v2.db import Base


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(
        "customer_id",
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
        nullable=False
    )
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(18), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp(), nullable=False)

    transactions = relationship("Transaction", backref='customer', secondary='customer')
