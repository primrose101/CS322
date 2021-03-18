import Tokens
import StatusTypes
import math


class InputHandler:

    def __init__(self) -> None:
        self.status = StatusTypes.STATUS_OK

    # assumes token_stream has only every variable separated by comma
    def assign_inputs(self, token_stream, inputs, variables):

        if (idens := len(token_stream)) != (values := len(inputs)):
            self.status = f'Expected {idens} inputs but got {values}'
            return

        for identifier, input_value in zip(token_stream, inputs):

            type = variables[identifier[1]]['type']

            if type == Tokens.STRING:
                variables[identifier[1]]['value'] = f'"{input_value}"'
            elif type == Tokens.CHAR:
                if len(input_value) != 1:
                    self.status = f'Invalid input value for type \'char\''
                    return
                variables[identifier[1]]['value'] = f'\'{input_value}\''
            elif type == Tokens.INT:
                if not (input_value.lstrip('-')).isnumeric():
                    self.status = f'Invalid input value for type \'int\''
                    return
                variables[identifier[-1]]['value'] = int(input_value)
            elif type == Tokens.FLOAT:
                try:
                    variables[identifier[-1]]['value'] = float(input_value)
                except:
                    self.status = f'Invalid input value for type \'float\''
                    return
            else:  # if boolean
                if input_value not in ('TRUE', 'FALSE'):
                    self.status = f'Invalid input value for type \'boolean\''
                    return
                variables[identifier[-1]]['value'] = input_value

        return variables
