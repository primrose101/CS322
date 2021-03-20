import Tokens
import StatusTypes


class StringExpression:

    def __init__(self) -> None:
        self.status = StatusTypes.STATUS_OK
        self.error_string = None

    def evaluate(self, token_stream, variables):

        result = str()

        for token_type, token in token_stream:
            if token_type == Tokens.CONCATENATOR:
                continue
            if token_type == Tokens.IDENTIFIER:
                temp = variables[token]['value']
                if (type := variables[token]['type']) in (Tokens.STRING, Tokens.CHAR):
                    # [1:-1] --> removes single/double quotes
                    string_value = temp[1:-1]
                elif type in (Tokens.INT, Tokens.FLOAT):
                    string_value = str(temp)
                else:  # if BOOL_TRUE or BOOL FALSE
                    string_value = temp
            elif token_type == Tokens.STRING:
                string_value = self.process_string(token[1:-1])
            else:  # if Tokens.CHAR
                string_value = token[1] if token[1] != '#' else '\n'

            result += string_value

        return f'"{result}"'

    def process_string(self, string):
        processed = str()

        length = len(string)

        i = 0
        while i < length:
            if string[i] == '[':
                if i + 2 < length and string[i+2] == ']':
                    processed += string[i+1]
                    i += 3
                else:
                    self.status = StatusTypes.STATUS_MISSING_CLOSE_BRAC
                    self.error_string = f'"{string}"'
                    break
            elif string[i] == ']':
                self.status = StatusTypes.STATUS_MISSING_OPEN_BRAC
                self.error_string = f'"{string}"'
                break
            elif string[i] == '#':
                processed += '\n'
                i += 1
            else:
                processed += string[i]
                i += 1

        return processed
