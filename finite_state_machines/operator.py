"""
string_input : String -> the text input to lexicalize
index : int -> where the index is currently at during lexicalization
"""


def operator_fsm(string_input, index):
    i = index

    table = [
        (1, 2),
        (2, 2),
        (2, 2),
    ]
    state = 0
    infut = 0
    string_length = len(string_input)

    while i < string_length:
        if string_input[i] in ('+', '-', '*', '/', '%', '&', '(', ')'):
            infut = 0
        else:
            infut = 1

        state = table[state][infut]

        if state == 2:
            break

        i += 1

    return i - index
