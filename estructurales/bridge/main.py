from refined_abstraction import ClassicCreditCard
from concrete_implementor import SecureCreditCard, UnsecureCreditCard


def main():
    card = ClassicCreditCard(UnsecureCreditCard())
    card.make_payment()

    card = ClassicCreditCard(SecureCreditCard())
    card.make_payment()


if __name__ == '__main__':
    main()
