from abstraction import CreditCard
from implementor import ICreditCard


class ClassicCreditCard(CreditCard):
    def __init__(self, card: ICreditCard):
        super().__init__(card)

    def make_payment(self):
        self._card.make_payment()
