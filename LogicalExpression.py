import Tokens
import StatusTypes


class LogicalExpression:

    def __init__(self):
        self.value = 0
        self.status = StatusTypes.STATUS_OK
        self. precedence = {
            "NOT": 3,
            "OR": 3,
            "AND": 3,
            "<>": 2,
            "==": 2,
            ">=": 2,
            "<=": 2,
            "<": 2,
            ">": 2,
            "(": 1,
        }
        self.op_list = [
            'AND',
            'OR',
            '==',
            '<=',
            '<>',
            '>=',
            '>',
            '<'
        ]

    def evaluate(self, token_stream, varmap={}):
        try:
            stack = self.infixToPostfix(token_stream, varmap)

            return self.calculate(stack)
        except IndexError:
            self.status = StatusTypes.STATUS_MISSING_OPEN_PAR
            return False
        except TypeError:
            self.status = StatusTypes.STATUS_MISSING_CLOSE_PAR
            return False

    def token_to_value(self, tokenized_value):
        return tokenized_value == 'TRUE'

    def raw_to_token(self, raw_bool):
        return 'TRUE' if raw_bool else 'FALSE'

    def infixToPostfix(self, token_stream, varmap):
        opStack = []
        postfixList = []

        for token, token_value in token_stream:
            if token == Tokens.IDENTIFIER:
                postfixList.append(varmap[token_value]['value'])
            elif token in [Tokens.BOOL_TRUE, Tokens.BOOL_FALSE]:
                postfixList.append(self.token_to_value(token_value))
            elif token == Tokens.INT:
                postfixList.append(int(token_value))
            elif token == Tokens.FLOAT:
                postfixList.append(float(token_value))
            elif token in (Tokens.STRING, Tokens.CHAR):
                postfixList.append(token_value)
            elif token == Tokens.PAREN_OPEN:
                opStack.append(token_value)
            elif token == Tokens.PAREN_CLOSE:
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:  # token is operator
                while (opStack) and \
                        (self.precedence[opStack[-1]] >= self.precedence[token_value]):
                    postfixList.append(opStack.pop())
                opStack.append(token_value)

        while opStack:
            postfixList.append(opStack.pop())

        if '(' in postfixList:
            raise TypeError
        return postfixList

    def calculate(self, stack):
        values = []
        for token in stack:
            if token in self.op_list:
                right = values.pop()
                left = values.pop()
                if token == 'AND':
                    val = left and right
                elif token == 'OR':
                    val = left or right
                elif token == '==':
                    val = left == right
                elif token == '<>':
                    val = left != right
                elif token == '>':
                    val = left > right
                elif token == '>=':
                    val = left >= right
                elif token == '<':
                    val = left < right
                elif token == '<=':
                    val = left <= right
                values.append(val)
            else:
                values.append(token)

        return values[0]
