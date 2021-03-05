from LogicalExpression import LogicalExpression
from MathExpression import MathExpression
from Lexer import Lexer
from Parser import Parser
import Tokens

statement = """VAR world, hello = "Hey" AS STRING
VAR fl AS FLOAT
VAR in AS INT
VAR ch AS CHAR
VAR bl AS BOOL
START
INPUT: fl, in
in = 1 + 2 / 3 * 1.0 % 100
hello = "hello" & "world"
bl = TRUE && FALSE == TRUE <= FALSE >= || TRUE
OUTPUT: hello & "hello"
STOP"""

math_expression = 'in = ((3 + 9) / 3 * 6 % 5)'
boolean_expression = 'bl = 100 && FALSE == (TRUE || FALSE ) == 100.0'
string_expression = "'hey' & 'you'"

lexer = Lexer()
parser = Parser()
math_evaluator = MathExpression()
logic_evaluator = LogicalExpression()
variables = dict()

for line in boolean_expression.split('\n'):
    token_stream = lexer.lexicalize(line)
    # print(token_stream[2:])
    value = logic_evaluator.evaluate(token_stream[2:], variables)
    print(value)
    print(parser.parse(token_stream))
