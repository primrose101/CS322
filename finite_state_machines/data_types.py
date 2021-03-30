def int_lexer(string_input, index):
    i = index
    state_table = [[1, 2],
                   [1, 2],
                   [2, 2], ]

    state = 0
    infut = 0
    string_length = len(string_input)
    while i != string_length:
        if string_input[i].isdigit():
            infut = 0
        else:
            infut = 1
        state = state_table[state][infut]
        if state == 2:
            break
        i += 1
    return i - index


def intUnary_lexer(string_input, index):
    i = index
    state_table = [[1, 1, 1, 2],
                   [2, 2, 1, 2],
                   [2, 2, 2, 2], ]

    state = 0
    infut = 0
    string_length = len(string_input)
    while i != string_length:
        if string_input[i] == '-':
            infut = 0
        elif string_input[i] == '+':
            infut = 1
        elif string_input[i].isdigit():
            infut = 2
        else:
            infut = 3
        state = state_table[state][infut]
        if state == 2:
            break
        i += 1
    return i - index


def float_lexer(string_input, index):
    i = index
    state_table = [[1, 3, 3],
                   [1, 2, 3],
                   [2, 3, 3],
                   [3, 3, 3], ]

    state = 0
    infut = 0
    string_length = len(string_input)
    while i != string_length:
        if string_input[i].isdigit():
            infut = 0
        elif string_input[i] == '.':
            infut = 1
        else:
            infut = 2
        state = state_table[state][infut]
        if state == 3:
            break
        i += 1
    return i - index


def floatUnary_lexer(string_input, index):
    i = index
    state_table = [[1, 1, 1, 3, 3],
                   [3, 3, 1, 2, 3],
                   [3, 3, 2, 3, 3],
                   [3, 3, 3, 3, 3], ]

    state = 0
    infut = 0
    string_length = len(string_input)
    while i != string_length:
        if string_input[i] == '-':
            infut = 0
        elif string_input[i] == '+':
            infut = 1
        elif string_input[i].isdigit():
            infut = 2
        elif string_input[i] == '.':
            infut = 3
        else:
            infut = 4
        state = state_table[state][infut]
        if state == 3:
            break
        i += 1
    return i - index


def char_lexer(string_input, index):
    i = index
    state_table = [(1, 4),
                   (4, 2),
                   (3, 4),
                   (4, 4),
                   (4, 4)]

    state = 0
    infut = 0
    string_length = len(string_input)
    while i != string_length:
        if string_input[i] == '\'':
            infut = 0
        else:
            infut = 1
        state = state_table[state][infut]
        if state == 4:
            break
        i += 1
    return i - index


def string_lexer(string_input, index):
    i = index
    state_table = [(1, 3),
                   (2, 1),
                   (3, 3),
                   (3, 3)]

    state = 0
    infut = 0
    string_length = len(string_input)
    while i != string_length:
        if string_input[i] == '"':
            infut = 0
        else:
            infut = 1
        state = state_table[state][infut]
        if state == 3:
            break
        i += 1
    return i - index


def true_bool_lexer(string_input, index):
    i = index
    state_table = [[1, 7, 7, 7, 7, 7],
                   [7, 2, 7, 7, 7, 7],
                   [7, 7, 3, 7, 7, 7],
                   [7, 7, 7, 4, 7, 7],
                   [7, 7, 7, 7, 5, 7],
                   [6, 7, 7, 7, 7, 7],
                   [7, 7, 7, 7, 7, 7],
                   [7, 7, 7, 7, 7, 7], ]

    state = 0
    infut = 0
    string_length = len(string_input)
    while i != string_length:
        if string_input[i] == '"':
            infut = 0
        elif string_input[i] == 'T':
            infut = 1
        elif string_input[i] == 'R':
            infut = 2
        elif string_input[i] == 'U':
            infut = 3
        elif string_input[i] == 'E':
            infut = 4
        else:
            infut = 5
        state = state_table[state][infut]
        if state == 7:
            break
        i += 1
    return i - index


def false_bool_lexer(string_input, index):
    i = index
    state_table = [[1, 8, 8, 8, 8, 8, 8],
                   [8, 2, 8, 8, 8, 8, 8],
                   [8, 8, 3, 8, 8, 8, 8],
                   [8, 8, 8, 4, 8, 8, 8],
                   [8, 8, 8, 8, 5, 8, 8],
                   [8, 8, 8, 8, 8, 6, 8],
                   [7, 8, 8, 8, 8, 8, 8],
                   [8, 8, 8, 8, 8, 8, 8],
                   [8, 8, 8, 8, 8, 8, 8], ]
    state = 0
    infut = 0
    string_length = len(string_input)
    while i != string_length:
        if string_input[i] == '"':
            infut = 0
        elif string_input[i] == 'F':
            infut = 1
        elif string_input[i] == 'A':
            infut = 2
        elif string_input[i] == 'L':
            infut = 3
        elif string_input[i] == 'S':
            infut = 4
        elif string_input[i] == 'E':
            infut = 5
        else:
            infut = 6
        state = state_table[state][infut]
        if state == 8:
            break
        i += 1
    return i - index


def unary_lexer(string_input, index):
    i = index
    state_table = [[1, 1, 2, 2],
                   [2, 2, 1, 2],
                   [2, 2, 2, 2], ]

    state = 0
    infut = 0
    string_length = len(string_input)
    while i != string_length:
        if string_input[i] == '-':
            infut = 0
        elif string_input[i] == '+':
            infut = 1
        elif string_input[i].isdigit():
            infut = 2
        else:
            infut = 3
        state = state_table[state][infut]
        if state == 2:
            break
        i += 1
    return i - index
