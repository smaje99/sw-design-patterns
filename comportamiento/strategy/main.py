from context import Context
from concrete_strategy import LowerStrategyTextFormatter
from concrete_strategy import UpperStrategyTextFormatter
from concrete_strategy import CapitalizeStrategyTextFormatter


def main():
    context = Context(CapitalizeStrategyTextFormatter())
    context.publish_text('SergiO maJé')


if __name__ == '__main__':
    main()
