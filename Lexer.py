import re
import Tokens


class Lexer:
    status = 0

    def __init__(self):
        status = 0

    def parse(self, statement):
        statement = self.replaceStmt(statement)
        tokens = statement.split(" ")
        arrforlex = []
        actualvalue = []
        ctr = 0

        for token in tokens:
            ctr = ctr+1
            type = 0
            if token == '':
                continue
            else:
                type = self.checktoken(token)
                print(token, type)
            if type == Tokens.ERROR:
                arrforlex.clear()
                arrforlex.insert(0, Tokens.ERROR)
                arrforlex.insert(1, 'Unexpected token: ' + token)
                break
            else:
                arrforlex.insert(ctr, type)
            actualvalue.insert(ctr, token)
        return arrforlex, actualvalue

    def checktoken(self, token):
        if(re.match(r'VAR [a-zA-Z_$][a-zA-Z_$0-9]*$', token)):
            type = Tokens.KW_VAR
        elif(re.match(r'^OUTPUT:\s*', token)):
            type = Tokens.KW_OUTPUT
        elif (re.match(r'((-*)\d+\.\d+)', token)):
            type = Tokens.FLOAT
        elif (re.match(r'((-*)\d)', token)):
            type = Tokens.INT
        elif (re.match(r'(^[a-zA-Z_$][a-zA-Z_$0-9]*$)', token)):
            type = self.parseAlpha(token)
        elif (re.match(r'.', token)):
            type = self.parseSpecial(token)
        elif(token.isidentifier()):
            type = Tokens.IDENTIFIER
        else:
            type = Tokens.ERROR
        return type

    def parseAlpha(self, token):
        if token == 'AS':
            type = Tokens.KW_AS
        elif token == 'INT':
            type = Tokens.KW_INT
        elif token == 'CHAR':
            type = Tokens.CHAR
        elif token == 'FLOAT':
            type = Tokens.KW_FLOAT
        elif token == 'BOOL':
            type = Tokens.KW_BOOLEAN
        elif token == 'START':
            type = Tokens.KW_START
        elif token == 'STOP':
            type = Tokens.KW_STOP
        elif token == 'OUTPUT':
            type = Tokens.KW_OUTPUT
        elif token == 'AND':
            type = Tokens.AND
        elif token == 'OR':
            type = Tokens.OR
        elif token == 'NOT':
            type = Tokens.NOT
        elif token == 'TRUE':
            type = Tokens.TRUE
        elif token == 'FALSE':
            type = Tokens.FALSE
        return type

    def parseSpecial(self, token):
        if token == '=':
            type = Tokens.EQUALS
        elif token == '(':
            type = Tokens.PAREN_OPEN
        elif token == ')':
            type = Tokens.PAREN_CLOSE
        elif token == '+':
            type = Tokens.PLUS
        elif token == '-':
            type = Tokens.MINUS
        elif token == '*':
            type = Tokens.MULTIPLY
        elif token == '/':
            type = Tokens.DIVIDE
        elif token == '%':
            type = Tokens.MODULO
        elif token == '[':
            type = Tokens.ESCAPE_OPEN
        elif token == ']':
            type = Tokens.ESCAPE_CLOSE
        elif token == '>':
            type = Tokens.GREATER_THAN
        elif token == '>=':
            type = Tokens.GREATER_OR_EQUAL
        elif token == '<':
            type = Tokens.LESS_THAN
        elif token == '<=':
            type = Tokens.LESS_OR_EQUAL
        elif token == '<>':
            type = Tokens.LOGIC_EQUAL
        elif token == '!=':
            type = Tokens.NOT_EQUAL
        else:
            type = Tokens.ERROR
        return type

    def replaceStmt(self, statement):
        symbol_list = [',', '+', '*', '/', '=', '(', ')', '==', '<=', '>=', '<>', ","]

        for symbol in symbol_list:
            statement = statement.replace(symbol, '' + {symbol} + '')

        return statement
