from decimal import Decimal
from dateutil.parser import parse


from bricklane_platform.models.card import Card
from bricklane_platform.models.bank import Bank
from bricklane_platform.config import PAYMENT_FEE_RATE


class Payment(object):

    customer_id = None
    date = None
    amount = None
    fee = None
    card_id = None
    bank_account = None

    def __init__(self, data=None, source='card'):

        if not data:
            return

        if source == 'card':
            self.customer_id = int(data["customer_id"])
            self.date = parse(data["date"])

            total_amount = Decimal(data["amount"])
            self.fee = total_amount * PAYMENT_FEE_RATE
            self.amount = total_amount - self.fee

            card = Card()
            card.card_id = int(data["card_id"])
            card.status = data["card_status"]
            self.card = card
        elif source == 'bank':
            self.customer_id = int(data["customer_id"])
            self.date = parse(data["date"])

            total_amount = Decimal(data["amount"])
            self.fee = total_amount * PAYMENT_FEE_RATE
            self.amount = total_amount - self.fee

            bank = Bank()
            bank.bank_account_id = int(data["bank_account_id"])

    def is_successful(self):
        return self.card.status == "processed"