from concrete_element import OfertaGasolina, OfertaVuelos
from concrete_visitor import ClassicCreditCardVisitor, BlackCreditCardVisitor


def main():
    oferta = OfertaGasolina()
    oferta.accept(BlackCreditCardVisitor())

    oferta = OfertaVuelos()
    oferta.accept(ClassicCreditCardVisitor())


if __name__ == '__main__':
    main()
