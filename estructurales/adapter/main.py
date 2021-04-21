from concrete_target import CreditCard


def main():
    card = CreditCard()
    try:
        card.pay('classic')
        card.pay('gold')
        card.pay('black')
        card.pay('silver')
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    main()
