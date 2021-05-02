from typing import Dict

from flyweight import Enemy
from concrete_flyweight import Private, Detective


__enemies: Dict[str, Enemy] = {}


def get_enemy(type_enemy: str) -> Enemy:
    global __enemies
    enemy: Enemy = __enemies.get(type_enemy)
    if not enemy:
        if type_enemy == 'Private':
            print('Soldado he sido creado')
            enemy = Private()
        elif type_enemy == 'Detective':
            print('Detective he sido creado')
            enemy = Detective()
        else:
            print('No se ha creado enemigo')

        __enemies[type_enemy] = enemy
    return enemy
