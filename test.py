from Interpreter import interpret

# test your statements here
statement = """
VAR num AS INT
VAR bool AS BOOLEAN
START
num = 100 + (((66 - 30))) * (-2 / 1) 
bool = TRUE && (((FALSE && TRUE || FALSE)))
OUTPUT: "Hello, World!" & "[#"
OUTPUT: bool
STOP
"""

# put your inputs here
test_inputs = '66 30 15\n22 55'


print(interpret(statement, test_inputs))
