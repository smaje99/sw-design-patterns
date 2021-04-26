from component import Credit


class CreditDecorator(Credit):
    def __init__(self, credit: Credit):
        self._credit = credit

    def show_credit(self) -> str:
        return self._credit.show_credit()
