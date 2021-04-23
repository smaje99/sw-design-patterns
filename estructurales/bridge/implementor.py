from abc import ABC, abstractmethod


class ICreditCard(ABC):
    @abstractmethod
    def make_payment(self): pass
