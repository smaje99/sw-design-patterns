from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def do_payment(self): pass
