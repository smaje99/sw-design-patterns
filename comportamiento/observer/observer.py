from abc import ABC, abstractmethod

from comportamiento.observer.data import Semaforo


class Observer(ABC):
    @abstractmethod
    def update(self,semaforo: Semaforo): pass
