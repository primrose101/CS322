"""
string_input : String -> the text input to lexicalize
index : int -> where the index is currently at during lexicalization
"""


def logicalop_fsm(string_input, index):
    i = index

    table = [
        (1, 2, 3, 4, 5, 5),
        (6, 5, 5, 5, 5, 5),
        (6, 5, 6, 5, 5, 5),
        (6, 5, 5, 5, 5, 5),
        (5, 5, 5, 6, 5, 5),
        (5, 5, 5, 5, 6, 5),
        (5, 5, 5, 5, 5, 5),
    ]
    state = 0
    infut = 0
    string_length = len(string_input)

    while i < string_length:
        if string_input[i] == '=':
            infut = 0
        elif string_input[i] == '<':
            infut = 1
        elif string_input[i] == '>':
            infut = 2
        elif string_input[i] == '&':
            infut = 3
        elif string_input[i] == '|':
            infut = 4
        else:
            infut = 5

        state = table[state][infut]

        if state == 5:
            break

        i += 1

    return i - index
