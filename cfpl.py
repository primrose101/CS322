
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def compile(program, inputs):
    token_stream = Lexer(program)
    parser = Parser(token_stream)
    interpreter = Interpreter(parser, inputs)

    try:
        result = interpreter.interpret()
    except Exception as e:
        return e

    return interpreter.output
