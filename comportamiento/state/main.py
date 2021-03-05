from comportamiento.state.concrete_state import Vibration, Silent
from comportamiento.state.context import MobileAlertStateContext


def main():
    context = MobileAlertStateContext()
    context.alert()

    context = Vibration()
    context.alert()

    context = Silent()
    context.alert()


if __name__ == '__main__':
    main()
