import uuid

from sqlalchemy import Column, UUID, Enum, Double, Integer, TIMESTAMP, func
from sqlalchemy.orm import relationship

from api.v2.db import Base
from api.v2.product.product_enums import ProductType, ProductCategory, ProductSubcategory


class Product(Base):
    __tablename__ = "products"
    id = Column(
        "product_id",
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
        nullable=False
    )
    type = Column("product_type", Enum(ProductType), nullable=False, index=True)
    category = Column("product_category", Enum(ProductCategory), nullable=False, index=True)
    subcategory = Column(Enum(ProductSubcategory), nullable=False, index=True)
    inventory = Column(Integer, nullable=False, default=0)
    price = Column(Double, nullable=False)
    cost = Column("product_cost", Double, nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp(), nullable=False)

    transactions = relationship("Transaction", backref="product", secondary='product')
