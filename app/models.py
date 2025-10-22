from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from enum import Enum, auto

class OrderStatus(str, Enum):
    """Enum for tracking order status."""
    PENDING = "pending"
    PROCESSING = "processing"
    PAID = "paid"
    FAILED = "failed"
    CANCELLED = "cancelled"

class User(SQLModel, table=True):
    """User model with subscription tracking."""
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    name: str
    created_at: datetime = Field(default_factory=datetime.now)

    # Subscription fields - placeholders for the future story
    stripe_customer_id: Optional[str] = None
    subscription_status: Optional[str] = None

    # Relationships
    orders: List["Order"] = Relationship(back_populates="user")

class Order(SQLModel, table=True):
    """Order model that will be updated by Stripe webhooks."""
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(foreign_key="user.id")
    amount: float
    currency: str = "usd"
    status: OrderStatus = Field(default=OrderStatus.PENDING)
    stripe_payment_intent_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    # Relationships
    user: Optional[User] = Relationship(back_populates="orders")

class WebhookEvent(SQLModel, table=True):
    """Model to track webhook events (useful for debugging)."""
    id: Optional[int] = Field(default=None, primary_key=True)
    stripe_event_id: str = Field(index=True)
    event_type: str
    data: str  # JSON string of event data
    processed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)