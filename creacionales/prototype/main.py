import prototype_factory as factory
from prototype_factory import CardType


def main():
    factory.load_card()

    visa = factory.get_instance(CardType.VISA)
    amex = factory.get_instance(CardType.AMEX)

    print(visa.card())
    print(amex.card())


if __name__ == '__main__':
    main()
