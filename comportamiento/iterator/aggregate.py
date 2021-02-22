from abc import ABC, abstractmethod

from iterator import Iterator


class List(ABC):
    @abstractmethod
    def iterator(self) -> Iterator: pass
