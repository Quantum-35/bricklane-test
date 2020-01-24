import csv

from bricklane_platform.models.payment import Payment


class PaymentProcessor(object):

    def get_payments(self, csv_path, source):
        payments = []
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            if source == 'card':
                for row in reader:
                    payments.append(Payment(row, source))
            elif source == 'bank':
                for row in reader:
                    print(row)
                    pass

        return payments

    def verify_payments(self, payments, source):
        successful_payments = []
        print('0-->', payments)
        for payment in payments:
            if payment.is_successful():
                successful_payments.append(payment)

        return successful_payments
