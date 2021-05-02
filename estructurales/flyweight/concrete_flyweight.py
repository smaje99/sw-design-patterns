from flyweight import Enemy


class Private(Enemy):
    def __init__(self):
        self.__weapon: str = None
        self.__LIFE = 200

    def set_weapon(self, weapon: str) -> str:
        self.__weapon = weapon
        return f'El arma del soldado es: {self.__weapon}'

    def life_points(self) -> str:
        return f'La vida de un soldado es: {self.__LIFE}'


class Detective(Enemy):
    def __init__(self):
        self.__weapon: str = None
        self.__LIFE = 1000

    def set_weapon(self, weapon: str) -> str:
        self.__weapon = weapon
        return f'El arma del teniente es: {self.__weapon}'

    def life_points(self) -> str:
        return f'La vida de un teniente es: {self.__LIFE}'
