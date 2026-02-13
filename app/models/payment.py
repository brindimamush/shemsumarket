from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.db.base import Base, UUIDMixin


class Payment(Base, UUIDMixin):
    __tablename__ = "payments"

    order_id = mapped_column(
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    gateway_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    transaction_reference: Mapped[str | None] = mapped_column(
        String(255),
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="pending",
        nullable=False,
    )

    paid_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
    )

    order = relationship("Order", back_populates="payment")
