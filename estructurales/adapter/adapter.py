from target import Payment
from adaptee import BlackCreditCard, GoldCreditCard


class Adapter(Payment):
    def pay(self, type: str):
        secure_credit_card = None
        if type == 'black':
            secure_credit_card = BlackCreditCard()
        elif type == 'gold':
            secure_credit_card = GoldCreditCard()

        secure_credit_card.pay_with_secure()
