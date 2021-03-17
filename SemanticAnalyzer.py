from StatusTypes import STATUS_OK
import Tokens
import StatusTypes


class SemanticAnalyzer:

    def __init__(self):
        self.status = StatusTypes.STATUS_OK

    # works
    # checks if assignments on variables matches on type declaration
    def semantic_analyze(self, token_stream, statement_type, variables):
        is_valid = True
        if statement_type == Tokens.ST_DECLARATION:
            is_valid = self.is_valid_declaration(token_stream)
        elif statement_type == Tokens.ST_ASSIGNMENT_MATH_INT:
            is_valid = self.is_valid_int_statement(token_stream, variables)
        elif statement_type == Tokens.ST_ASSIGNMENT_LOGIC:
            is_valid = self.is_valid_bool_statement(token_stream, variables)
        elif statement_type == Tokens.ST_ASSIGNMENT_MATH_FLOAT:
            is_valid = self.is_valid_float_statement(token_stream, variables)
        elif statement_type == Tokens.ST_ASSIGNMENT_STRICT_STRING:
            is_valid = self.is_valid_string_statement(token_stream, variables)
        else:
            is_valid = self.is_valid_char_statement(token_stream, variables)

        return is_valid

    def is_valid_declaration(self, token_stream):
        type_of_iden = token_stream[-1][0]
        length = len(token_stream)
        for i in range(length):
            token_type = token_stream[i][0]
            if token_type == Tokens.EQUALS:
                value_type = token_stream[i+1][0]
                if (value_type == Tokens.STRING and type_of_iden == Tokens.KW_STRING) or \
                    (value_type == Tokens.CHAR and type_of_iden == Tokens.KW_CHAR) or \
                    (value_type == Tokens.INT and type_of_iden == Tokens.KW_INT) or \
                    (value_type == Tokens.FLOAT and type_of_iden == Tokens.KW_FLOAT) or \
                        ((value_type == Tokens.BOOL_TRUE or value_type == Tokens.BOOL_FALSE) and type_of_iden == Tokens.KW_BOOLEAN):
                    continue
                else:
                    self.status = StatusTypes.STATUS_INVALID_ASSIGNMENT
                    return False

        return True

    def is_valid_int_statement(self, token_stream, variables):
        is_valid = True
        for token_type, value in token_stream:
            if token_type in (Tokens.PLUS, Tokens.MINUS, Tokens.DIVIDE, Tokens.MULTIPLY, Tokens.MODULO, Tokens.EQUALS, Tokens.INT):
                continue
            if token_type == Tokens.IDENTIFIER:
                if variables.has_key(value):
                    if variables[value]['type'] == Tokens.INT:
                        continue
                    else:
                        is_valid = False
                        break
                else:
                    self.status = StatusTypes.STATUS_UNDEFINED_VARIABLE
                    is_valid = False
                    break

            if token_type == Tokens.FLOAT:
                self.status = StatusTypes.STATUS_FLOAT_ON_INT_STATEMENT
                is_valid = False
                break

        return is_valid

    # checks if
    def is_valid_float_statement(self, token_stream, variables):
        is_valid = True
        for token_type, value in token_stream:
            if token_type in (Tokens.PLUS, Tokens.MINUS, Tokens.DIVIDE, Tokens.MULTIPLY, Tokens.EQUALS, Tokens.INT, Tokens.FLOAT):
                continue
            if token_type == Tokens.IDENTIFIER:
                if variables.has_key(value):
                    if variables[value]['type'] in (Tokens.FLOAT, Tokens.INT):
                        continue
                    else:
                        self.status = StatusTypes.STATUS_ERROR_ON_FLOAT
                        is_valid = False
                        break
                else:
                    self.status = StatusTypes.STATUS_UNDEFINED_VARIABLE
                    is_valid = False
                    break
            if token_type == Tokens.MODULO:
                is_valid = False
                self.status = StatusTypes.STATUS_FLOAT_ON_INT_STATEMENT
                break

        return is_valid

    def is_valid_string_statement(self, token_stream, variables):
        is_valid = True
        for token_type, value in token_stream:
            if token_type in (Tokens.CONCATENATOR, Tokens.STRING, Tokens.CHAR):
                continue
            if token_type == Tokens.IDENTIFIER:
                if variables.has_key(value):
                    if variables[value]['type'] in (Tokens.STRING, Tokens.CHAR):
                        continue
                    else:
                        self.status = StatusTypes.STATUS_ERROR_ON_STRING
                        is_valid = False
                        break
                else:
                    self.status = StatusTypes.STATUS_UNDEFINED_VARIABLE
                    is_valid = False
                    break

        return is_valid

    def is_valid_bool_statement(self, token_stream, variables):

        # logical operators and equals
        ignored_values = (Tokens.LOGIC_EQUAL, Tokens.EQUALS, Tokens.AND, Tokens.OR, Tokens.GREATER_THAN, Tokens.GREATER_OR_EQUAL,
                          Tokens.LESS_THAN, Tokens.LESS_OR_EQUAL, Tokens.NOT_EQUAL, Tokens.BOOL_TRUE, Tokens.BOOL_FALSE)

        data_types = (Tokens.BOOL_TRUE, Tokens.BOOL_FALSE, Tokens.INT, Tokens.FLOAT, Tokens.STRING, Tokens.CHAR)

        is_valid = True

        for token_type, value in token_stream:
            if token_type in ignored_values:
                continue
            if token_type == Tokens.IDENTIFIER:
                if variables.has_key(value):
                    if variables[value]['type'] in data_types:
                        continue
                    else:
                        self.status = StatusTypes.STATUS_ERROR_ON_BOOL
                        is_valid = False
                        break
                else:
                    self.status = StatusTypes.STATUS_UNDEFINED_VARIABLE
                    is_valid = False
                    break

        return is_valid

    def is_valid_char_statement(self, token_stream, variables):
        if len(token_stream) != 3:
            self.status = StatusTypes.STATUS_ERROR_ON_CHAR
            return False

        if token_stream[2][0] == Tokens.IDENTIFIER:
            if variables.has_key(value := token_stream[2][1]):
                if variables[value]['type'] == Tokens.CHAR:
                    return True
                else:
                    self.status = StatusTypes.STATUS_ERROR_ON_CHAR
                    is_valid = False
            else:
                self.status = StatusTypes.STATUS_UNDEFINED_VARIABLE
                is_valid = False

        return True
