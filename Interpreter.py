
from Parser import Parser
from Lexer import Lexer
import StatusTypes
import Tokens


def interpret(lines, custom_input):

    inputs = [line for line in custom_input.split('\n')]

    status = StatusTypes.STATUS_MISSING_START

    lexer = Lexer()
    parser = Parser()
    state = 0

    state_table = [
        (0, 1, 3, 3),
        (3, 3, 1, 2),
        (3, 3, 3, 3)
    ]

    for line in lines.split('\n'):
        input = 0
        if not line:
            continue

        token_stream = lexer.lexicalize(line)
        stmt_type = parser.parse_tokens(token_stream)
        print(line)
        print(stmt_type)

        if stmt_type == Tokens.ST_DECLARATION:
            input = 0
        elif stmt_type == Tokens.ST_START:
            input = 1
            status = StatusTypes.STATUS_MISSING_STOP

        elif stmt_type in (Tokens.ST_ASSIGNMENT_LOGIC, Tokens.ST_ASSIGNMENT_MATH, Tokens.ST_ASSIGNMENT_STRING, Tokens.ST_INPUT, Tokens.ST_OUTPUT):
            input = 2

            # TODO: determine and separate math assignments (float, int) and string_assignment (string, char)

        elif stmt_type == Tokens.ST_STOP:
            input = 3
            status = StatusTypes.STATUS_OK

        state = state_table[state][input]
        if state == 3:
            break

    return 'Code is complete' if state == 2 else 'Code has errors'
