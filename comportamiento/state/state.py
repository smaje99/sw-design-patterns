from abc import ABC, abstractmethod


class MobileAlertState(ABC):
    @abstractmethod
    def alert(self): pass
