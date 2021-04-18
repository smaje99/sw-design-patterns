from concrete_classes import Paypal, Visa


def main():
    payment = Visa()
    payment.make_payment()
    print()
    payment = Paypal()
    payment.make_payment()


if __name__ == '__main__':
    main()
