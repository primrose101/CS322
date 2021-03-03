import Tokens


class MathExpression:

    def __init__(self):
        self.value = 0

    def evaluate(self, token_stream, varmap={}, e_type=Tokens.INT):
        stack = self.infixToPostfix(token_stream, varmap)
        final_value = self.calculate(stack)

        if e_type == Tokens.INT:
            final_value = int(final_value)

        return final_value

    def calculate(self, stack):
        values = []
        for token in stack:
            if token in ['+', '-', '*', '/', '%']:
                right = values.pop()
                left = values.pop()
                if token == '+':
                    val = left + right
                elif token == '-':
                    val = left - right
                elif token == '*':
                    val = left * right
                elif token == '/':
                    val = left / right
                elif token == '%':
                    val = left % right
                values.append(val)
            else:
                values.append(token)
        return values[0]

    def infixToPostfix(self, token_stream, varmap):
        prec = {}
        prec["*"] = 3
        prec["/"] = 3
        prec["%"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1

        opStack = []
        postfixList = []

        for token, token_value in token_stream:
            if (token == Tokens.IDENTIFIER):
                postfixList.append(varmap[token_value]['value'])
            elif (token == Tokens.INT):
                postfixList.append(int(token_value))
            elif (token == Tokens.FLOAT):
                postfixList.append(float(token_value))
            elif token == Tokens.PAREN_OPEN:
                opStack.append(token_value)
            elif token == Tokens.PAREN_CLOSE:
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not len(opStack) == 0) and \
                        (prec[opStack[-1]] >= prec[token_value]):
                    postfixList.append(opStack.pop())
                opStack.append(token_value)

        while not len(opStack) == 0:
            postfixList.append(opStack.pop())

        return postfixList
