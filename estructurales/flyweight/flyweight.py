from abc import ABC, abstractmethod


class Enemy(ABC):
    @abstractmethod
    def set_weapon(self, weapon: str) -> str: pass

    @abstractmethod
    def life_points(self) -> str: pass
