from abc import ABC, abstractmethod


class StrategyTextFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str: pass
