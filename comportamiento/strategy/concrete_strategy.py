from strategy import StrategyTextFormatter


class LowerStrategyTextFormatter(StrategyTextFormatter):
    def format(self, text: str) -> str:
        return text.lower()


class UpperStrategyTextFormatter(StrategyTextFormatter):
    def format(self, text: str) -> str:
        return text.upper()


class CapitalizeStrategyTextFormatter(StrategyTextFormatter):
    def format(self, text: str) -> str:
        return text.capitalize()
