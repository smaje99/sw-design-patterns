from abstract_expression import Expression


class TerminalExpression(Expression):
    def __init__(self, text: str):
        self.text = text

    def interpret(self, context: str) -> bool:
        return self.text in context
