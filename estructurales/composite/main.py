from leaf import CuentaAhorro, CuentaCorriente
from composite import CuentaComposite


def main():
    cuentas = [
        CuentaCorriente(1_000, "Alberto"),
        CuentaAhorro(20_000, "Freddy")
    ]

    composite = CuentaComposite(cuentas)
    composite.show_account_name()
    print(f'$ {composite.get_amount()}')


if __name__ == '__main__':
    main()
