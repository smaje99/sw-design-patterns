from terminal_expression import TerminalExpression
from non_terminal_expression import OrExpression, AndExpression


def main():
    zero = TerminalExpression('0')
    one = TerminalExpression('1')

    contain_bool = OrExpression(zero, one)
    contains_one_and_zero = AndExpression(zero, one)

    print(contain_bool.interpret('zero'))
    print(contain_bool.interpret('0'))

    print(contains_one_and_zero.interpret('0'))
    print(contains_one_and_zero.interpret('0, 1'))


if __name__ == '__main__':
    main()
