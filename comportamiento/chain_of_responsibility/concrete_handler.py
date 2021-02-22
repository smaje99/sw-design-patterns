from handler import ApproveLoanChain


class Gold(ApproveLoanChain):
    def credit_card_request(self, total_loan: int) -> str:
        return 'Esta solicitud de tarjeta de crédito la maneja la tarjeta Gold.' \
            if total_loan <= 10_000 \
            else self.next.credit_card_request(total_loan)


class Platinum(ApproveLoanChain):
    def credit_card_request(self, total_loan: int) -> str:
        return 'Esta solicitud de tarjeta de crédito la maneja la tarjeta Platinum.' \
            if 10_000 < total_loan <= 50_000 \
            else self.next.credit_card_request(total_loan)


class Black(ApproveLoanChain):
    def credit_card_request(self, total_loan: int) -> str:
        return 'Esta solicitud de tarjeta de crédito la maneja la tarjeta Black.' \
            if total_loan > 50_000 \
            else self.next.credit_card_request(total_loan)


class Card(ApproveLoanChain):
    def __create_chain_card(self):
        """
        Cadena de responsabilidad de las Tarjetas
        """
        gold = Gold()
        self.next = gold

        platinum = Platinum()
        gold.next = platinum

        black = Black()
        platinum.next = black

    def credit_card_request(self, total_loan: int) -> str:
        if total_loan <= 0: raise ValueError()
        self.__create_chain_card()
        return self.next.credit_card_request(total_loan)
