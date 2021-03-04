from comportamiento.observer.data import Semaforo
from comportamiento.observer.observer import Observer


class Peaton(Observer):
    def update(self, semaforo: Semaforo):
        if 'ROJO' == semaforo.status.strip().upper():
            print('Semaforo Verde para Peaton -> Peaton SI puede pasar')
        else:
            print('Semaforo Rojo para Peaton -> Peaton NO puede pasar')


class Coche(Observer):
    def update(self, semaforo: Semaforo):
        if 'ROJO' == semaforo.status.strip().upper():
            print('Semaforo Rojo para Coche -> Coche NO puede pasar')
        else:
            print('Semaforo Verde para Coche -> Coche SI puede pasar')
