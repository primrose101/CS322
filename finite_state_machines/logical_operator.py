"""
string_input : String -> the text input to lexicalize
index : int -> where the index is currently at during lexicalization
"""


def logicalop_fsm(string_input, index):
    i = index

    table = [
        (1, 2, 3, 4, 5, 6),
        (7, 6, 6, 6, 6, 6),
        (7, 5, 7, 6, 6, 6),
        (7, 6, 6, 6, 6, 6),
        (6, 6, 6, 7, 6, 6),
        (6, 6, 6, 6, 7, 6),
        (6, 6, 6, 6, 6, 6),
        (6, 6, 6, 6, 6, 6),
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

        if state == 6:
            break

        i += 1

    return i - index


def and_fsm(string_input, index):
    i = index

    table = [
        [1, 4, 4, 4],
        [4, 2, 4, 4],
        [4, 4, 3, 4],
        [4, 4, 4, 4],
        [4, 4, 4, 4],
    ]

    state = 0
    inputstate = 0

    string_length = len(string_input)

    while i != string_length:
        if string_input[i] == 'A':
            inputstate = 0
        elif string_input[i] == 'N':
            inputstate = 1
        elif string_input[i] == 'D':
            inputstate = 2
        else:
            inputstate = 3

        state = table[state][inputstate]

        if state == 4:
            break

        i += 1

    return i - index


def or_fsm(string_input, index):
    i = index

    table = [
        [1, 3, 3],
        [3, 2, 3],
        [3, 3, 3],
        [3, 3, 3],
    ]

    state = 0
    inputstate = 0

    string_length = len(string_input)

    while i != string_length:
        if string_input[i] == 'O':
            inputstate = 0
        elif string_input[i] == 'R':
            inputstate = 1
        else:
            inputstate = 2

        state = table[state][inputstate]

        if state == 3:
            break

        i += 1

    return i - index
