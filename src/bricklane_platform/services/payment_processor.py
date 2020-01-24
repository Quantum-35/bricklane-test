import csv

from bricklane_platform.models.payment import Payment


class PaymentProcessor(object):

    def get_payments(self, csv_path, source):
        payments = []
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                payments.append(Payment(row, source))
        return payments


    def verify_payments(self, payments, source):
        successful_payments = []
        for payment in payments:
            print(payment.__dict__)
            if payment.is_successful(source):
                successful_payments.append(payment)

        return successful_payments
