from decimal import Decimal
from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, UUIDMixin


class OrderItem(Base, UUIDMixin):
    __tablename__ = "order_items"

    order_id = mapped_column(
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
    )

    product_id = mapped_column(
        ForeignKey("products.id", ondelete="SET NULL"),
        nullable=True,
    )

    quantity: Mapped[int] = mapped_column(nullable=False)

    unit_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
