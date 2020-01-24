from payment import Payment
from decimal import Decimal

from bricklane_platform.models.card import Card


class CardPayment(Payment):

    def __init__(self, data=None):
        if not data:
            return
        super(CardPayment, self).__init__(data)
        card = Card()
        card.card_id = int(data["card_id"])
        card.status = data["card_status"]
        self.card = card

    def is_successful(self):
        return self.card.status == "processed"