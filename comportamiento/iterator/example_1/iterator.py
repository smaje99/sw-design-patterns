from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def next(self): pass

    @abstractmethod
    def has_next(self) -> bool: pass

    @abstractmethod
    def current_item(self): pass
