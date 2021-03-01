from Lexer import Lexer

statement = """VAR world, hello = "Hey" as STRING
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

for line in statement.split('\n'):
    print(lexer.lexicalize(line))
