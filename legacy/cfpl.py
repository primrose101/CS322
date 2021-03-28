
from legacy.lexer import Lexer
from legacy.parser import Parser
from legacy.interpreter import Interpreter


def compile(program, inputs):
    token_stream = Lexer(program)
    parser = Parser(token_stream)
    interpreter = Interpreter(parser, inputs)

    try:
        result = interpreter.interpret()
        return interpreter.output
    except Exception as error:
        return error
