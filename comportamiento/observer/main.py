from time import sleep

from comportamiento.observer.concrete_observer import Coche, Peaton
from comportamiento.observer.concrete_subject import MessagePublisher
from comportamiento.observer.data import Semaforo


def main():
    coche = Coche()
    peaton = Peaton()
    message_publisher = MessagePublisher()

    message_publisher.attach(coche)
    message_publisher.attach(peaton)

    message_publisher.notify_all(Semaforo('ROJO'))
    sleep(30)
    message_publisher.notify_all(Semaforo('VERDE'))


if __name__ == '__main__':
    main()
