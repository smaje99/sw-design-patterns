from abc import ABC, abstractmethod


class Credit(ABC):
    @abstractmethod
    def show_credit(self) -> str: pass
