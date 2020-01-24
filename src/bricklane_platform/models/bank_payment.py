from payment import Payment
from decimal import Decimal

from bricklane_platform.models.bank import Bank


class BankPayment(Payment):

    def __init__(self, data=None):
        if not data:
            return
        super(BankPayment, self).__init__(data)
        bank = Bank()
        bank.bank_account_id = int(data["bank_account_id"])
        total_amount = Decimal(data["amount"])
        if self.amount < total_amount and self.amount > 1:
            bank.status='processed'
        else:
            bank.status='failed'

    def is_successful(self):
        return True