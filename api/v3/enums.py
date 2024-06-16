from enum import Enum

from sqlalchemy import String
from sqlalchemy.types import TypeDecorator


class Gender(str, Enum):
    NA = 'N/A'
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Availability(str, Enum):
    AVAILABLE_NOW = 'Available Now'
    DAYS_1_3 = '1-3 Days'
    DAYS_4_10 = '4-10 Days'
    DAYS_10_30 = '10-30 Days'
    NO_LONGER_AVAILABLE = 'No Longer Available'


class ChannelLevel1(str, Enum):
    WEBSITE = 'Website'
    CALL_CENTER = 'Call Center'
    MARKETPLACE = 'Marketplace'
    MOBILE_APP = 'Mobile App'
    PHYSICAL_STORE = 'Physical Store'


class ChannelLevel2(str, Enum):
    WALMART = 'Walmart'
    EBAY = 'EBay'
    AMAZON = 'Amazon'
    OUR_WEBSITE = 'Our Website'
    BEST_BUY = 'Best Buy'
    TARGET = 'Target'
    NEWEGG = 'Newegg'
    ETSY = 'Etsy'
    ALIBABA = 'Alibaba'
    SKROUTZ = 'Skroutz'
    PHYSICAL_STORE_1 = 'Physical Store 1'
    PHYSICAL_STORE_2 = 'Physical Store 2'


class PaymentMethod(str, Enum):
    CASH = 'Cash'
    CASH_ON_DELIVERY = 'Cash On Delivery'
    CREDIT_CARD = 'Credit Card'
    DEBIT_CARD = 'Debit Card'
    BANK_TRANSFER = 'Bank Transfer'
    AUTOPAY = 'Autopay'
    REWARD_POINTS = 'Reward Points'
    BUY_NOW_PAY_LATER = 'Buy Now Pay Later'
    CHEQUE = 'Cheque'
    MOBILE_WALLET = 'Mobile Wallet'


class OrderStatus(str, Enum):
    RECEIVED = 'Received'
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'
    REFUNDED = 'Refunded'


class TicketStatus(str, Enum):
    OPEN = 'Open'
    PROCESSING = 'Processing'
    RESOLVED = 'Resolved'
    UNRESOLVED = 'Unresolved'


channel_mapping = {
    ChannelLevel1.WEBSITE: [ChannelLevel2.AMAZON, ChannelLevel2.EBAY, ChannelLevel2.OUR_WEBSITE, ChannelLevel2.NEWEGG,
                            ChannelLevel2.ETSY, ChannelLevel2.ALIBABA],
    ChannelLevel1.CALL_CENTER: [ChannelLevel2.WALMART, ChannelLevel2.BEST_BUY, ChannelLevel2.TARGET],
    ChannelLevel1.MARKETPLACE: [ChannelLevel2.AMAZON, ChannelLevel2.EBAY, ChannelLevel2.ETSY, ChannelLevel2.ALIBABA],
    ChannelLevel1.MOBILE_APP: [ChannelLevel2.AMAZON, ChannelLevel2.EBAY, ChannelLevel2.OUR_WEBSITE,
                               ChannelLevel2.NEWEGG, ChannelLevel2.ETSY],
    ChannelLevel1.PHYSICAL_STORE: [ChannelLevel2.PHYSICAL_STORE_1, ChannelLevel2.PHYSICAL_STORE_2,
                                   ChannelLevel2.WALMART, ChannelLevel2.BEST_BUY, ChannelLevel2.TARGET]
}


# Without this class, SQLAlchemy will pass the Enum's Key Name instead of the desired String
class StringEnum(TypeDecorator):
    impl = String

    def __init__(self, enum_class, *args, **kwargs):
        self.enum_class = enum_class
        super().__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):
        if isinstance(value, self.enum_class):
            return value.value
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            return self.enum_class(value)
        return value
