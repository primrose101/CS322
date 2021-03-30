from legacy.cfpl import compile
from Interpreter import interpret


statements = """
VAR num1, num2 AS INT
START
INPUT: num1, num2
WHILE(num1 < num2)
START
num1 = num1+1
OUTPUT: "HEY" & "#"
STOP
STOP
"""

inputs = "3, 7"

if 'IF' in statements or 'WHILE' in statements:
    result = compile(statements, inputs)
else:
    result = interpret(statements, inputs)

print(result)
