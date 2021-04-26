from component import Credit


class Black(Credit):
    def show_credit(self) -> str:
        return 'El crédito es de $1.000.000'


class Gold(Credit):
    def show_credit(self) -> str:
        return 'El crédito es de $50.000'
