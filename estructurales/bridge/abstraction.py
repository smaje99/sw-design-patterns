from abc import ABC, abstractmethod

from implementor import ICreditCard


class CreditCard(ABC):
    def __init__(self, card: ICreditCard):
        self._card = card

    @abstractmethod
    def make_payment(self): pass
