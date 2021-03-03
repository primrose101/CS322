import Tokens

class MathExpression:

    def __init__(self):
        self.value = 0


    def evaluate(self, token, actualtoken, varmap):
        stack = self.infixToPostfix(token, actualtoken)
        val = self.calculate(stack, varmap)
        var = varmap.get(actualtoken[0])
        var[0] = val
        varmap[actualtoken[0]] = var
        return varmap

    def calculate(self, stack, varmap):
        values = []
        idx = 0
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
                val = varmap[token[0]]
                values.append(val)
            idx += 1
        return values[0]

    def infixToPostfix(self, tokenList, actualtoken):
        prec = {}
        prec["*"] = 3
        prec["/"] = 3
        prec["%"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        opStack = []
        postfixList = []
        idx = 0
        for token in tokenList:
            if idx == 0:
                idx += 1
                continue
            elif (token == Tokens.INT or
                token == Tokens.FLOAT):
                postfixList.append(actualtoken[idx])
            elif token == Tokens.PAREN_OPEN:
                opStack.append(actualtoken[idx])
            elif token == Tokens.PAREN_CLOSE:
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            elif token == Tokens.EQUALS:
                idx += 1
                continue
            else:
                while (not len(opStack) == 0) and \
                (prec[opStack[len(opStack)-1]] >= prec[actualtoken[idx]]):
                    postfixList.append(opStack.pop())
                opStack.append(actualtoken[idx])
            idx += 1

        while not len(opStack) == 0:
            postfixList.append(opStack.pop())
        return postfixList

            

