from concrete_element import OfertaVuelos, OfertaGasolina
from visitor import CreditCardVisitor


class ClassicCreditCardVisitor(CreditCardVisitor):
    def oferta_gasolina(self, oferta: OfertaGasolina):
        print("Descuento de 3% con tu tarjeta Classic")

    def oferta_vuelos(self, oferta: OfertaVuelos):
        print("Descuento de 5% con tu tarjeta Classic")


class BlackCreditCardVisitor(CreditCardVisitor):
    def oferta_gasolina(self, oferta: OfertaGasolina):
        print("Descuento de 10% con tu tarjeta Black")

    def oferta_vuelos(self, oferta: OfertaVuelos):
        print("Descuento de 25% con tu tarjeta Black")
