from abc import ABC, abstractmethod


class OfertaElement(ABC):
    @abstractmethod
    def accept(self, credit_card): pass
