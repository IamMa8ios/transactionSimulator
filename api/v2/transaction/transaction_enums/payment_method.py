import enum


class PaymentMethod(enum.StrEnum):
    cash = "Cash"
    cash_on_delivery = "Cash on Delivery"
    credit_card = "Credit Card"
    credit = "Credit"
    debit_card = "Debit Card"
    bank_transfer = "Bank Transfer"
