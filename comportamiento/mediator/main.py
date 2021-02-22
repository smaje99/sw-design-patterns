from concrete_colleague import ConcreteColleague1, ConcreteColleague2
from concrete_mediator import ConcreteMediator


def main():
    mediator = ConcreteMediator()
    user1 = ConcreteColleague1(mediator)
    user2 = ConcreteColleague2(mediator)

    mediator.user1 = user1
    mediator.user2 = user2

    print(user1.send('Hola soy user1'))
    print(user2.send('Hola user1, soy user2'))


if __name__ == '__main__':
    main()
