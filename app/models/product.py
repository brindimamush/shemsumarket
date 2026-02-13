from decimal import Decimal

from sqlalchemy import String, Text, ForeignKey, Boolean, Numeric, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, UUIDMixin, TimestampMixin


class Product(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "products"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)

    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    stock_quantity: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    company_id = mapped_column(
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False,
    )

    category_id = mapped_column(
        ForeignKey("categories.id", ondelete="SET NULL"),
        nullable=True,
    )

    # Relationships
    company = relationship("Company", back_populates="products")
    category = relationship("Category", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")

    __table_args__ = (
        Index("ix_products_is_active", "is_active"),
    )
