'''
Using this class assumes that the token_stream is a Tokens.ST_DECLARATION
and token_stream has already been parsed and semantically analyzed
'''
import Tokens


class DeclarationHandler:

    def handle_declaration(self, token_stream: list):
        variable_type = token_stream[-1][0]
        variables = dict()

        token_stream = token_stream[1:len(token_stream)-2]
        new_length = len(token_stream) - 1
        index = 0

        while(index < new_length):
            name = token_stream[index][0]
            if token_stream[index+1][0] == Tokens.EQUALS:
                value = self.set_value_by_type(token_stream[index+2][1], variable_type)
                variables[name] = {'value': value, 'type': variable_type}
                index += 4
            else:
                variables[name] = {'value': None, 'type': variable_type}
                index += 2

        return variables

    def set_value_by_type(self, value, type):
        if type == Tokens.KW_STRING or type == Tokens.KW_CHAR:
            return value[1:len(value)-1]  # remove quotes
        if type == Tokens.KW_INT:
            return int(value)
        if type == Tokens.KW_FLOAT:
            return float(value)
        if type == Tokens.KW_BOOLEAN:
            return value == Tokens.BOOL_TRUE

        return None
