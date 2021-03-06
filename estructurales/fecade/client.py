from estructurales.fecade.facade import CreditMarket


def main():
    credit_market = CreditMarket()
    credit_market.show_credit_gold()
    credit_market.show_credit_silver()
    credit_market.show_credit_black()


if __name__ == '__main__':
    main()
