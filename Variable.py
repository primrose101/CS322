import Tokens


class Variable:

    def __init__(self, name, data_type, value):
        self.name = name
        self.data_type = data_type
        self.value = value

    def exists(self, test_name):
        return self.name == test_name

    def matches(self, value):
        matches_string = self.data_type == Tokens.STRING and type(value) is str
        matches_char = self.data_type == Tokens.CHAR and type(value) is str and len(value) == 1
        matches_int = self.data_type == Tokens.INT and type(value) is int
        matches_float = self.data_type == Tokens.FLOAT and type(value) is float
        matches_boolean = self.data_type == Tokens.BOOL and type(value) is bool

        return matches_string or matches_char or matches_int or matches_float or matches_boolean

    def assign(self, value):
        if self.matches(value):
            self.value = value
