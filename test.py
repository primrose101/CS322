from cfpl import compile

code = """
VAR str AS CHAR
START
OUTPUT: "Hello World" & str
STOP 
"""

inputs = ''

print(compile(code, inputs))
