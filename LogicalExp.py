import Tokens

class LogicalExpression:

    def __init__(self):
        self.value = 0

    def evaluate(self, token, actualtoken, varmap):
            stack = self.infixToPostfix(token, actualtoken)
            result, val = self.assess(stack, varmap, vartype)
            var = varmap.get(actualtoken[0])
            var[0] = val
            varmap[actualtoken[0]] = var
        return result, varmap

    def infixToPostfix(self, tokenList, actualtoken):
        prec = {}
        prec["NOT"] = 2
        prec["OR"] = 2
        prec["AND"] = 2
        prec["<>"] = 3
        prec["=="] = 3
        prec[">="] = 3
        prec["<="] = 3
        prec["<"] = 3
        prec[">"] = 3
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

    def translateNumericValue(self, val, type):
        result = True
        if type == Tokens.INT:
            return True, int(val)
        elif type == Tokens.FLOAT:
            return True, float(val)
        else:
            return False, False

    def examinemathvar(self, varmap, left, right, operator):
        result = True
        val = False
        if operator == '<':
            val = left < right
        elif operator == '>':
            val = left > right
        elif operator == '<=':
            val = left <= right
        elif operator == '>=':
            val = left >= right
        elif operator == '==':
            val = left == right
        elif operator == '<>':
            val = left != right
        return result, val

    def examinelogvar(self, varmap, left, right, operator):
        result = True
        val = False
        if operator == 'AND':
            val = left and right
        elif operator == 'OR':
            val = left or right
        else:
            val = False
        return result, val

    def assess(self, stack, varmap, vartype):
        ari_arr = ['<', '>', '<=', '>=', '==', '<>']
        log_arr = ['AND', 'OR']
        values = []
        idx = 0
        result = True
        for token in stack:
            if token in ari_arr:
                right = values.pop()
                left = values.pop()
                result, val = self.examinemathvar(varmap, left, right, token)
                values.append(val)
            elif token in log_arr:
                right = values.pop()
                left = values.pop()
                if isinstance(left, bool) and isinstance(right, bool):
                    result, val = self.examinelogvar(varmap, left, right, token)
                    values.append(val)
                else:
                    result = False
            elif token == 'NOT':
                left = values.pop()
                if isinstance(left, bool):
                    val = not left
                    values.append(val)
                else:
                    result = False
            else:
                var = varmap.get(token)
                if var != None:
                    values.append(var[0])
                else:
                    l = LexAnalyzer()
                    type = l.checktoken(token)
                    result, val = self.translateNumericValue(token, type)
                    values.append(val)
            idx += 1
            if not result:
                break
        return result, values[0]