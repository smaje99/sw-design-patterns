from random import choice

import flyweight_factory as enemy_factory


def main():
    enemy_type = ['Private', 'Detective']
    weapon = ['Fusil',
              'Revolver',
              'Pistola',
              'Metralleta',
              'Lanza Granadas',
              '9mm']

    for _ in range(15):
        enemy = enemy_factory.get_enemy(choice(enemy_type))
        print(enemy.set_weapon(choice(weapon)))
        print(enemy.life_points())


if __name__ == '__main__':
    main()
