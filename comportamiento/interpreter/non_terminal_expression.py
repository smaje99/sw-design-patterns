from abstract_expression import Expression


class OrExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        self.expression1 = expression1
        self.expression2 = expression2

    def interpret(self, context: str) -> bool:
        return self.expression1.interpret(context) \
               or self.expression2.interpret(context)


class AndExpression(Expression):
    def __init__(self, expression1: Expression, expression2: Expression):
        self.expression1 = expression1
        self.expression2 = expression2

    def interpret(self, context: str) -> bool:
        return self.expression1.interpret(context) \
               and self.expression2.interpret(context)
