from InputHandler import InputHandler
from DeclarationHandler import DeclarationHandler
from LogicalExpression import LogicalExpression
from MathExpression import MathExpression
from SemanticAnalyzer import SemanticAnalyzer
from StringExpression import StringExpression
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
boolean_expression = 'he = 100 && FALSE == (TRUE || FALSE ) == 100.0'
string_expression = 'hey = "NI" & char & "[#]" & \'#\' & char'

dec_stmt_no_error = 'VAR hello = \'h\' AS STRING'
dec_stmt_no_values = 'VAR hey = 3.57, world = 4.0 AS FLOAT'

test_string = 'VAR hello, hey AS STRING\nINPUT: hey, hello'

test_inputs = 'hi! gwyneth,'


# semantics test

lexer = Lexer()
parser = Parser()
dec_handler = DeclarationHandler()
math_evaluator = MathExpression()
string_evaluator = StringExpression()
logic_evaluator = LogicalExpression()
semantics = SemanticAnalyzer()
input_handler = InputHandler()
inputs = test_inputs.split(' ')

variables = dict()

for line in test_string.split('\n'):
    token_stream = lexer.lexicalize(line)
    stmt_type = parser.parse_tokens(token_stream)
    print(stmt_type)
    print(token_stream)
    if stmt_type == Tokens.ST_DECLARATION:
        variables = dec_handler.handle_declaration(token_stream, variables)
    elif stmt_type == Tokens.ST_INPUT:
        variables = input_handler.assign_inputs(token_stream[2::2], inputs, variables)

    print(variables)
