from typing import List

from component import CuentaComponent


class CuentaComposite(CuentaComponent):
    def __init__(self, children: List[CuentaComponent] = None):
        self._children: List[CuentaComponent] = children if children else []

    def add_cuenta(self, cuenta: CuentaComponent):
        self._children.append(cuenta)

    def remove_cuenta(self, cuenta: CuentaComponent):
        self._children.remove(cuenta)

    def show_account_name(self):
        for child in self._children:
            child.show_account_name()

    def get_amount(self) -> float:
        # from functools import reduce
        # return reduce(lambda a, b: a + b, map(lambda child: child.get_amount(), self._children))
        return sum(map(lambda child: child.get_amount(), self._children))
