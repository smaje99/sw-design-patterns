from strategy import StrategyTextFormatter


class Context:
    def __init__(self, strategy: StrategyTextFormatter):
        self._strategy = strategy

    def publish_text(self, text):
        print(self._strategy.format(text))
