from InputHandler import InputHandler
from DeclarationHandler import DeclarationHandler
from LogicalExpression import LogicalExpression
from MathExpression import MathExpression
from SemanticAnalyzer import SemanticAnalyzer
from StringExpression import StringExpression
from Lexer import Lexer
from Parser import Parser
from Interpreter import interpret
import Tokens

# test your statements here
statement = """
VAR world, hello = "Hey" AS STRING
VAR fl = 108.5 AS FLOAT
VAR in = 112, in2, in3 AS INT
VAR ch = 'l', cl AS CHAR
VAR bl = TRUE AS BOOL
VAR b2 AS BOOL
VAR fl2 = 16.5 AS FLOAT
VAR in4 = 69 AS INT
VAR flval AS FLOAT
VAR charint AS STRING
START
INPUT: fl, in2, in3
in = 1 + 2 / 3 * 1
in = 3
world = "hello" & "world"
bl = TRUE && FALSE == TRUE <= FALSE >= TRUE
b2 = TRUE && FALSE
ch = '1'
charint = hello 
OUTPUT: hello & "hello" & world & in & in2 & '#' & "[#]" & bl & b2 & '#'
OUTPUT: charint & '#'
OUTPUT: bl & '#'
STOP
"""

# put your inputs here
test_inputs = '66 30 15'


print(interpret(statement, test_inputs))
