"""
string_input : String -> the text input to lexicalize
index : int -> where the index is currently at during lexicalization
"""


def iden_fsm(string_input, index):
    i = index

    table = [
        (1, 1, 4, 4),
        (1, 1, 1, 3),
        (4, 4, 4, 4),
        (4, 4, 4, 4),

    ]
    state = 0
    infut = 0
    string_length = len(string_input)

    while i < string_length:
        if string_input[i].isalpha():
            infut = 0
        elif string_input[i] == '_':
            infut = 1
        elif string_input[i].isdigit():
            infut = 2
        else:
            infut = 3

        state = table[state][infut]

        if state == 4:
            break

        i += 1

    return i - index


# test

print(iden_fsm('STRING123', 0))
