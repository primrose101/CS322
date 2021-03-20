
from InputHandler import InputHandler
from SemanticAnalyzer import SemanticAnalyzer
from LogicalExpression import LogicalExpression
from StringExpression import StringExpression
from MathExpression import MathExpression
from DeclarationHandler import DeclarationHandler
from Parser import Parser
from Lexer import Lexer
import StatusTypes
import Tokens


def interpret(lines, custom_input):

    inputs = [line for line in custom_input.split('\n')]

    input_index = 0
    completion_status = StatusTypes.STATUS_MISSING_START

    output = str()
    variables = {}

    lexer = Lexer()
    parser = Parser()
    dec_handler = DeclarationHandler()
    input_handler = InputHandler()
    math_evaluator = MathExpression()
    string_evaluator = StringExpression()
    logic_evaluator = LogicalExpression()
    semantics = SemanticAnalyzer()

    # values for state table
    state = 0
    infut = 0

    state_table = [
        (0, 1, 3, 3),
        (3, 3, 1, 2),
        (3, 3, 3, 3)
    ]

    for line_number, line in enumerate(lines.split('\n'), 1):

        is_valid = True

        if not line or line.startswith('*'):  # comment algorithm
            continue

        token_stream = lexer.lexicalize(line)
        stmt_type = parser.parse_tokens(token_stream)
        print(token_stream)
        print(stmt_type)
        if parser.status != StatusTypes.STATUS_OK:
            return f'At line {line_number}: {parser.status}'

        # debugging
        # print(stmt_type)
        # print(variables)

        # TODO: separate strict assignment types
        if stmt_type == Tokens.ST_DECLARATION:
            infut = 0
            if semantics.semantic_analyze(token_stream, stmt_type, variables):
                variables = dec_handler.handle_declaration(token_stream, variables)
                if not dec_handler.status == StatusTypes.STATUS_OK:
                    return f'At line {line_number}: {dec_handler.status}'
            else:
                return f'At line {line_number}: {semantics.status}'

        elif stmt_type == Tokens.ST_START:
            infut = 1
            completion_status = StatusTypes.STATUS_MISSING_STOP

        elif stmt_type in (Tokens.ST_ASSIGNMENT_LOGIC, Tokens.ST_ASSIGNMENT_MATH, Tokens.ST_ASSIGNMENT_STRING, Tokens.ST_INPUT, Tokens.ST_OUTPUT):
            infut = 2
            if stmt_type == Tokens.ST_INPUT:
                if semantics.semantic_analyze(token_stream, stmt_type, variables):
                    variables = input_handler.assign_inputs(token_stream[2::2], inputs[input_index], variables)
                    if not input_handler.status == StatusTypes.STATUS_OK:
                        return f'At line {line_number}: {input_handler.status}'
                    input_index += 1
                else:
                    return f'At line {line_number}: {semantics.status}'

            if stmt_type in (Tokens.ST_ASSIGNMENT_MATH, Tokens.ST_ASSIGNMENT_LOGIC, Tokens.ST_ASSIGNMENT_STRING):

                variable_name = token_stream[0][1]

                if stmt_type == Tokens.ST_ASSIGNMENT_STRING:
                    if variable_name in variables:
                        token_type = variables[variable_name]['type']
                        if token_type == Tokens.CHAR:
                            stmt_type = Tokens.ST_ASSIGNMENT_STRICT_CHAR
                        elif token_type == Tokens.STRING:
                            stmt_type = Tokens.ST_ASSIGNMENT_STRICT_STRING
                        else:
                            return f'At line {line_number}: Invalid assignment on type \'{token_type}\''
                    else:
                        return f'At line {line_number}: {StatusTypes.STATUS_UNDEFINED_VARIABLE}'

                elif stmt_type == Tokens.ST_ASSIGNMENT_MATH:
                    if variables and variable_name in variables:
                        token_type = variables[variable_name]['type']
                        if token_type == Tokens.INT:
                            stmt_type = Tokens.ST_ASSIGNMENT_STRICT_INT
                        elif token_type == Tokens.FLOAT:
                            stmt_type = Tokens.ST_ASSIGNMENT_STRICT_FLOAT
                        else:
                            return f'At line {line_number}: Invalid assignment on type \'{token_type}\''
                    else:
                        return f'At line {line_number}: {StatusTypes.STATUS_UNDEFINED_VARIABLE}'
                else:
                    if variable_name in variables:
                        token_type = variables[variable_name]['type']
                        if token_type in (Tokens.BOOL, Tokens.BOOL_TRUE, Tokens.BOOL_FALSE):
                            pass
                        else:
                            return f'At line {line_number}: Invalid assignment on type \'{token_type}\''
                    else:
                        return f'At line {line_number}: {StatusTypes.STATUS_UNDEFINED_VARIABLE}'

                is_valid = semantics.semantic_analyze(token_stream[2::], stmt_type, variables)

                if is_valid:
                    if stmt_type in (Tokens.ST_ASSIGNMENT_STRICT_CHAR, Tokens.ST_ASSIGNMENT_STRICT_STRING):
                        variables[variable_name]['value'] = string_evaluator.evaluate(token_stream[2::], variables)
                    elif stmt_type in (Tokens.ST_ASSIGNMENT_STRICT_FLOAT, Tokens.ST_ASSIGNMENT_STRICT_INT):
                        if stmt_type == Tokens.ST_ASSIGNMENT_STRICT_FLOAT:
                            e_type = Tokens.FLOAT
                        else:
                            e_type = Tokens.INT
                        variables[variable_name]['value'] = math_evaluator.evaluate(
                            token_stream[2::], variables, e_type)
                    else:
                        variables[variable_name]['value'] = logic_evaluator.evaluate(token_stream[2::], variables)
                else:
                    return f'At line {line_number}: {semantics.status}'

            if stmt_type == Tokens.ST_OUTPUT:
                if semantics.semantic_analyze(token_stream, stmt_type, variables):
                    temp = string_evaluator.evaluate(token_stream[2:], variables)
                    output += temp[1:-1]  # remove quotes
                else:
                    return f'At line {line_number}: {semantics.status}'

        elif stmt_type == Tokens.ST_STOP:
            infut = 3
            completion_status = StatusTypes.STATUS_OK

        state = state_table[state][infut]
        if state == 3:
            break

    if state == 2:
        return output
    else:
        return completion_status
