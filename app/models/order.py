from decimal import Decimal
from sqlalchemy import String, ForeignKey, Numeric, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, UUIDMixin, TimestampMixin


class Order(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "orders"

    telegram_user_id: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="pending",
        nullable=False,
    )

    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    company_id = mapped_column(
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False,
    )

    company = relationship("Company", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
    payment = relationship("Payment", back_populates="order", uselist=False)

    __table_args__ = (
        Index("ix_orders_telegram_user_id", "telegram_user_id"),
    )
