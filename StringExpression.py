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
                string_value = variables[token]['value']
            elif token_type == Tokens.STRING:
                # [1:-2] --> remove single quotes or double quotes
                string_value = self.process_string(token[1:len(token)-1])
            else:  # if Tokens.CHAR
                string_value = token[1] if token[1] != '#' else '\n'

            result += string_value

        return result

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
                    self.status = StatusTypes.STATUS_MISSING_OPEN_BRAC
                    self.error_string = string
                    break
            elif string[i] == '#':
                processed += '\n'
                i += 1
            else:
                processed += string[i]
                i += 1

        return processed
