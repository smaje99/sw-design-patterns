from abc import ABC, abstractmethod


class CreditCardVisitor(ABC):
    @abstractmethod
    def oferta_gasolina(self, oferta): pass

    @abstractmethod
    def oferta_vuelos(self, oferta): pass
