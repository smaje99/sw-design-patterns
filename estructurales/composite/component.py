from abc import ABC, abstractmethod


class CuentaComponent(ABC):
    @abstractmethod
    def show_account_name(self): pass

    @abstractmethod
    def get_amount(self) -> float: pass
