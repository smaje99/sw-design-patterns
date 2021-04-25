from component import CuentaComponent


class CuentaAhorro(CuentaComponent):
    def __init__(self, amount: float, name: str):
        self._amount = amount
        self._name = name

    def show_account_name(self):
        print(self._name)

    def get_amount(self) -> float:
        return self._amount


class CuentaCorriente(CuentaComponent):
    def __init__(self, amount: float, name: str):
        self._amount = amount
        self._name = name

    def show_account_name(self):
        print(self._name)

    def get_amount(self) -> float:
        return self._amount
