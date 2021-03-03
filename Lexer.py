import re

import StatusTypes
import Tokens


class Lexer:
    status = StatusTypes.STATUS_OK

    def lexicalize(self, statement):
        statement = self.replaceStmt(statement)
        tokens = statement.split(" ")
        token_stream = []

        for token in tokens:
            if token == '':
                continue
            token_type = self.checktoken(token)
            token_stream.append([token_type, token])
            if token == Tokens.ERROR:
                status = StatusTypes.STATUS_UNIDENTIFIED_TOKEN
                break

        return token_stream

    def checktoken(self, token):
        if token.startswith('"') and token.endswith('"'):
            type = Tokens.STRING
        elif token.startswith("'") and token.endswith("'") and len(token) == 3:
            type = Tokens.CHAR
        elif (re.match(r'((-*)\d+\.\d+)', token)):
            type = Tokens.FLOAT
        elif (re.match(r'((-*)\d)', token)):
            type = Tokens.INT
        else:
            type = self.parseAlpha(token)
        return type

    def parseAlpha(self, token):
        if token == 'VAR':
            type = Tokens.KW_VAR
        elif token == 'INPUT':
            type = Tokens.KW_INPUT
        elif token == 'OUTPUT':
            type = Tokens.KW_OUTPUT
        elif token == 'AS':
            type = Tokens.KW_AS
        elif token == 'INT':
            type = Tokens.KW_INT
        elif token == 'CHAR':
            type = Tokens.KW_CHAR
        elif token == 'FLOAT':
            type = Tokens.KW_FLOAT
        elif token == 'BOOL':
            type = Tokens.KW_BOOLEAN
        elif token == 'STRING':
            type = Tokens.KW_STRING
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
            type = Tokens.BOOL_TRUE
        elif token == 'FALSE':
            type = Tokens.BOOL_FALSE
        elif token == '&':
            type = Tokens.CONCATENATOR
        elif token == '=':
            type = Tokens.EQUALS
        elif token == ',':
            type = Tokens.COMMA
        elif token == ':':
            type = Tokens.COLON
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
        elif token == '==':
            type = Tokens.LOGIC_EQUAL
        elif token == '!=':
            type = Tokens.NOT_EQUAL
        elif token == '||':
            type = Tokens.OR
        elif token == '&&':
            type = Tokens.AND
        elif token == '~':
            type = Tokens.NOT
        elif token.isidentifier():
            type = Tokens.IDENTIFIER
        else:
            type = Tokens.ERROR
        return type

    def replaceStmt(self, statement):
        symbol_list = [',', '+', '*', '/', '==', '(', ')', '=', '<', '>', '<=', '>=', '&&', ':', '&', '||']

        for symbol in symbol_list:
            statement = statement.replace(symbol, ' ' + symbol + ' ')
            statement = statement.replace('<  =', '<=')
            statement = statement.replace('>  =', '>=')
            statement = statement.replace('=  =', '==')
            statement = statement.replace('&  &', '&&')

        print(statement)
        return statement
