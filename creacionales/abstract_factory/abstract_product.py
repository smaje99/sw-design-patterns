from abc import ABC, abstractmethod


class Card(ABC):
    @abstractmethod
    def card_type(self) -> str: pass

    @abstractmethod
    def card_number(self) -> str: pass


class PaymentMethod(ABC):
    @abstractmethod
    def do_payment(self) -> str: pass
