import uuid

from sqlalchemy import Column, UUID, func, String, DateTime, CheckConstraint, UniqueConstraint, Index
from sqlalchemy.orm import relationship

from api.v3.db import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column("product_id", UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    title = Column(String(255), nullable=False)
    brand = Column(String(255), nullable=False)
    description = Column(String(255), default='', nullable=False)
    type = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    subcategory = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    variants = relationship("ProductVariant", back_populates="product")

    __table_args__ = (
        CheckConstraint('price >= 0', name='check_price'),
        CheckConstraint('cost >= 0', name='check_cost'),
        CheckConstraint('updated_at >= created_at', name='check_updated_at'),
        UniqueConstraint('title', 'brand', name='_title_brand_uc'),
        Index('idx_products_title', 'title'),
        Index('idx_products_brand', 'brand'),
        Index('idx_products_category', 'category'),
        Index('idx_products_subcategory', 'subcategory')
    )
