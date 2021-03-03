from Lexer import Lexer
from Parser import Parser

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

lexer = Lexer()
parser = Parser()
variables = dict()

for line in statement.split('\n'):
    token_stream = lexer.lexicalize(line)
    print(token_stream)
    print(parser.parse(token_stream))
