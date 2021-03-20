def int_lexer(string_input, index):
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
    state_table = [[1, 5, 5, 5, 5],
                   [5, 2, 5, 5, 5],
                   [5, 5, 3, 5, 5],
                   [5, 5, 5, 4, 5],
                   [5, 5, 5, 5, 5],
                   [5, 5, 5, 5, 5], ]

    state = 0
    infut = 0
    string_length = len(string_input)
    while i != string_length:
        if string_input[i] == 'T':
            infut = 0
        elif string_input[i] == 'R':
            infut = 1
        elif string_input[i] == 'U':
            infut = 2
        elif string_input[i] == 'E':
            infut = 3
        else:
            infut = 4
        state = state_table[state][infut]
        if state == 5:
            break
        i += 1
    return i - index


def false_bool_lexer(string_input, index):
    i = index
    state_table = [[1, 6, 6, 6, 6, 6],
                   [6, 2, 6, 6, 6, 6],
                   [6, 6, 3, 6, 6, 6],
                   [6, 6, 6, 4, 6, 6],
                   [6, 6, 6, 6, 5, 6],
                   [6, 6, 6, 6, 6, 6],
                   [6, 6, 6, 6, 6, 6], ]

    state = 0
    infut = 0
    string_length = len(string_input)
    while i != string_length:
        if string_input[i] == 'F':
            infut = 0
        elif string_input[i] == 'A':
            infut = 1
        elif string_input[i] == 'L':
            infut = 2
        elif string_input[i] == 'S':
            infut = 3
        elif string_input[i] == 'E':
            infut = 4
        else:
            infut = 5
        state = state_table[state][infut]
        if state == 6:
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
