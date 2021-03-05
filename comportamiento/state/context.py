from comportamiento.state.concrete_state import Sound
from comportamiento.state.state import MobileAlertState


class MobileAlertStateContext:
    def __init__(self):
        self.__current_state = Sound()

    @property
    def state(self) -> MobileAlertState:
        return self.__current_state

    @state.setter
    def state(self, state: MobileAlertState):
        self.__current_state = state

    def alert(self):
        self.__current_state.alert()
