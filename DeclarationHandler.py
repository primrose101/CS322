'''
Using this class assumes that the token_stream is a Tokens.ST_DECLARATION
and token_stream has already been parsed and semantically analyzed
'''
import Tokens
import StatusTypes


class DeclarationHandler:

    def __init__(self) -> None:
        self.status = StatusTypes.STATUS_OK

    def handle_declaration(self, token_stream, variables):
        variable_type = token_stream[-1][0]

        token_stream = token_stream[1:-2]
        new_length = len(token_stream)
        index = 0

        while(index < new_length):
            name = token_stream[index][1]
            if token_stream[index][0] == Tokens.IDENTIFIER:
                if name in variables:
                    self.status = f'Variable \'{name}\' is already defined.'
                if index + 1 < new_length and token_stream[index+1][0] == Tokens.EQUALS:
                    value = self.set_value_by_type(token_stream[index+2][1], variable_type)
                    variables[name] = {'value': value, 'type': self.set_variable_by_keyword(variable_type)}
                    index += 4
                else:
                    variables[name] = {'value': None, 'type': self.set_variable_by_keyword(variable_type)}
                    index += 2

        return variables

    def set_value_by_type(self, value, type):
        if type == Tokens.KW_STRING or type == Tokens.KW_CHAR:
            return value  # remove quotes
        if type == Tokens.KW_INT:
            return int(value)
        if type == Tokens.KW_FLOAT:
            return float(value)
        if type == Tokens.KW_BOOLEAN:
            return value == Tokens.BOOL_TRUE

    def set_variable_by_keyword(self, variable_type):
        if variable_type == Tokens.KW_STRING:
            return Tokens.STRING
        if variable_type == Tokens.KW_CHAR:
            return Tokens.CHAR
        if variable_type == Tokens.KW_INT:
            return Tokens.INT
        if variable_type == Tokens.KW_FLOAT:
            return Tokens.FLOAT
        if variable_type == Tokens.KW_BOOLEAN:
            return Tokens.BOOL

        return None
