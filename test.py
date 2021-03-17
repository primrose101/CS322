from DeclarationHandler import DeclarationHandler
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

dec_stmt_no_error = 'VAR hello = "hello" AS STRING'
dec_stmt_no_values = 'VAR hey = "a value", world AS STRING'

lexer = Lexer()
parser = Parser()
dec_handler = DeclarationHandler()
math_evaluator = MathExpression()
logic_evaluator = LogicalExpression()
variables = dict()

for line in dec_stmt_no_values.split('\n'):
    token_stream = lexer.lexicalize(line)
    stmt_type = parser.parse_tokens(token_stream)
    print(token_stream)
    if stmt_type == Tokens.ST_DECLARATION:
        variables = dec_handler.handle_declaration(token_stream, variables)
        print(variables)
