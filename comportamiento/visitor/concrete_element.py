from visitor import CreditCardVisitor
from element import OfertaElement


class OfertaVuelos(OfertaElement):
    def accept(self, credit_card: CreditCardVisitor):
        credit_card.oferta_vuelos(self)


class OfertaGasolina(OfertaElement):
    def accept(self, credit_card: CreditCardVisitor):
        credit_card.oferta_gasolina(self)
