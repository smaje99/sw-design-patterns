from module import Credit


class Gold(Credit):
    def show_credit(self):
        print('Gold card tiene un crédito de 5.000')


class Silver(Credit):
    def show_credit(self):
        print('Silver card tiene un crédito de 200.000')


class Black(Credit):
    def show_credit(self):
        print('Black card tiene un crédito de 1.000.000')
