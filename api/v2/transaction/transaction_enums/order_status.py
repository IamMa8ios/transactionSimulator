import enum


class OrderStatus(enum.StrEnum):
    received = "Received"
    processing = "Processing"
    shipped = "Shipped"
    cancelled = "Cancelled"
    completed = "Completed"
    refunded = "Refunded"
