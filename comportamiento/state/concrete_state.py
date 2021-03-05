from comportamiento.state.state import MobileAlertState


class Vibration(MobileAlertState):
    def alert(self):
        print('Vibrando')


class Silent(MobileAlertState):
    def alert(self):
        print('Silencio')


class Sound(MobileAlertState):
    def alert(self):
        print('Sonido')
