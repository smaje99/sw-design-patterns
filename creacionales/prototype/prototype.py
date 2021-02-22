from abc import ABC, abstractmethod


class PrototypeCard(ABC):
    @abstractmethod
    def card(self) -> str: pass

    @abstractmethod
    def clone(self): pass
