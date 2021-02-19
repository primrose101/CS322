import re


def interpret(lines):

    state = 0

    state_table = [
        (0, 1, 3, 3),
        (3, 3, 1, 2),
        (3, 3, 3, 3)
    ]

    for line in lines:
        if not line:
            continue
        if re.match('\AVAR', line):
            input = 0
        elif line == 'START':
            input = 1
        elif line == 'STOP':
            input = 3
        else:               # line is a statement
            input = 2

        state = state_table[state][input]
        if state == 3:
            break

    return 'Code is complete' if state == 2 else 'Code has errors'
