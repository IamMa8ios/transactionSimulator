import uuid

from sqlalchemy import Column, UUID, ForeignKey, String, Integer, DateTime, func, CheckConstraint, UniqueConstraint, \
    Index, Double
from sqlalchemy.orm import relationship

from api.v3.db import Base


class ProductVariant(Base):
    __tablename__ = 'product_variants'

    id = Column("variant_id", UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.product_id'), nullable=False)
    color = Column(String(255), nullable=False)
    pattern = Column(String(255), default='Solid', nullable=False)
    size = Column(String(5), nullable=False)
    image = Column(String(255), unique=True, nullable=False)
    inventory = Column(Integer, default=0, nullable=False)
    availability = Column(String(19), default='No Longer Available', nullable=False)
    price = Column(Double, nullable=False)
    cost = Column(Double, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    product = relationship("Product", back_populates="variants")
    customer_order_items = relationship("CustomerOrderItem", back_populates="variant")
    backorder_shipments = relationship("BackorderShipment", back_populates="variant")

    __table_args__ = (
        CheckConstraint('inventory >= 0', name='check_inventory'),
        CheckConstraint(
            "availability in ('Available Now', '1-3 Days', '4-10 Days', '10-30 Days', 'No Longer Available')",
            name='check_availability'),
        CheckConstraint('updated_at >= created_at', name='check_updated_at'),
        UniqueConstraint('product_id', 'color', 'pattern', 'size', name='_product_color_pattern_size_uc'),
        Index('idx_product_variations_product_id', 'product_id'),
        Index('idx_product_variations_color', 'color'),
        Index('idx_product_variations_pattern', 'pattern'),
        Index('idx_product_variations_size', 'size')
    )
