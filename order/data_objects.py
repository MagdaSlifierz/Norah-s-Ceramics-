from enum import Enum


class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    DISPATCHED = "dispatched"
    SHIPPED = "shipped"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
