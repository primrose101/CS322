from Interpreter import interpret

# test your statements here
statement = """
START
OUTPUT: "Hi" & ""
STOP
"""

# put your inputs here
test_inputs = '66 30 15\n22 55'


print(interpret(statement, test_inputs))
