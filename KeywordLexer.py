"""
string_input : String -> the text input to lexicalize
index : int -> where the index is currently at during lexicalization
"""
def kwstart_fsm(string_input, index):
    i = index 

    table = [
        [1,6,6,6,6,6],
        [6,2,6,6,6,6],
        [6,6,3,6,6,6],
        [6,6,6,4,6,6],
        [6,5,6,6,6,6],
        [6,6,6,6,6,6],
        [6,6,6,6,6,6],
    ]

    state = 0
    inputstate = 0

    string_length = len(string_input)

    while i != string_length:
        if string_input[i] == 'S':
            inputstate = 0
        elif string_input[i] == 'T':
            inputstate = 1
        elif string_input[i] == 'A':
            inputstate = 2
        elif string_input[i] == 'R':
            inputstate = 3
        elif string_input[i] == 'T':
            inputstate = 4
        else:
            inputstate = 5

        state = table[state][inputstate]

        if state == 6:
            break

        i += 1

    return i - index


def kwstop_fsm(string_input, index):
    i = index

    table = [
        [1,5,5,5,5],
        [5,2,5,5,5],
        [5,5,3,5,5],
        [5,5,5,4,5],
        [5,5,5,5,5], 
        [5,5,5,5,5],         
    ]

    state = 0
    inputstate = 0

    string_length = len(string_input)

    while i != string_length:
        if string_input[i] == 'S':
            inputstate = 0
        elif string_input[i] == 'T':
            inputstate = 1
        elif string_input[i] == 'O':
            inputstate = 2
        elif string_input[i] == 'P':
            inputstate = 3
        else:
            inputstate = 4

        state = table[state][inputstate]

        if state == 5:
            break

        i += 1

    return i - index

def kwinteger_fsm(string_input, index):
    i = index

    table = [
        [1,8,8,8,8,8,8,8],
        [8,2,8,8,8,8,8,8],
        [8,8,3,8,8,8,8,8],
        [8,8,8,4,8,8,8,8],
        [8,8,8,8,5,8,8,8],
        [8,8,8,6,8,8,8,8],
        [8,8,8,8,8,8,7,8],
        [8,8,8,8,8,8,8,8],
        [8,8,8,8,8,8,8,8],
               
    ]

    state = 0
    inputstate = 0

    string_length = len(string_input)

    while i != string_length:
        if string_input[i] == 'I':
            inputstate = 0
        elif string_input[i] == 'N':
            inputstate = 1
        elif string_input[i] == 'T':
            inputstate = 2
        elif string_input[i] == 'E':
            inputstate = 3
        elif string_input[i] == 'G':
            inputstate = 4
        elif string_input[i] == 'E':
            inputstate = 5
        elif string_input[i] == 'R':
            inputstate = 6
        else:
            inputstate = 7

        state = table[state][inputstate]

        if state == 8:
            break

        i += 1

    return i - index

def kwstring_fsm(string_input, index):
    i = index

    table = [
        [1,7,7,7,7,7,7],
        [7,2,7,7,7,7,7],
        [7,7,3,7,7,7,7],
        [7,7,7,4,7,7,7],
        [7,7,7,7,5,7,7],
        [7,7,7,7,7,6,7],
        [7,7,7,7,7,7,7],
        [7,7,7,7,7,7,7],
    ]

    state = 0
    inputstate = 0

    string_length = len(string_input)

    while i != string_length:
        if string_input[i] == 'S':
            inputstate = 0
        elif string_input[i] == 'T':
            inputstate = 1
        elif string_input[i] == 'R':
            inputstate = 2
        elif string_input[i] == 'I':
            inputstate = 3
        elif string_input[i] == 'N':
            inputstate = 4
        elif string_input[i] == 'G':
            inputstate = 5
        else:
            inputstate = 6

        state = table[state][inputstate]

        if state == 7:
            break

        i += 1

    return i - index

def kwfloat_fsm(string_input, index):
    i = index

    table = [
        [1,6,6,6,6,6],
        [6,2,6,6,6,6],
        [6,6,3,6,6,6],
        [6,6,6,4,6,6],
        [6,6,6,6,5,6],
        [6,6,6,6,6,6],
        [6,6,6,6,6,6],
    ]

    state = 0
    inputstate = 0

    string_length = len(string_input)

    while i != string_length:
        if string_input[i] == 'F':
            inputstate = 0
        elif string_input[i] == 'L':
            inputstate = 1
        elif string_input[i] == 'O':
            inputstate = 2
        elif string_input[i] == 'A':
            inputstate = 3
        elif string_input[i] == 'T':
            inputstate = 4
        else:
            inputstate = 5

        state = table[state][inputstate]

        if state == 6:
            break

        i += 1

    return i - index

def kwbool_fsm(string_input, index):
    i = index

    table = [
        [1,5,5,5,5],
        [5,2,5,5,5],
        [5,3,5,5,5],
        [5,5,5,4,5],
        [5,5,5,5,5], 
        [5,5,5,5,5],         
    ]

    state = 0
    inputstate = 0

    string_length = len(string_input)

    while i != string_length:
        if string_input[i] == 'B':
            inputstate = 0
        elif string_input[i] == 'O':
            inputstate = 1
        elif string_input[i] == 'O':
            inputstate = 2
        elif string_input[i] == 'L':
            inputstate = 3
        else:
            inputstate = 4

        state = table[state][inputstate]

        if state == 5:
            break

        i += 1

    return i - index


def kwout_fsm(string_input, index):
    i = index

    table = [
        [1,4,4,4],
        [4,2,4,4],
        [4,4,3,4],
        [4,4,4,4],
        [4,4,4,4],
    ]

    state = 0
    inputstate = 0

    string_length = len(string_input)

    while i != string_length:
        if string_input[i] == 'O':
            inputstate = 0
        elif string_input[i] == 'U':
            inputstate = 1
        elif string_input[i] == 'T':
            inputstate = 2
        else:
            inputstate = 3

        state = table[state][inputstate]

        if state == 4:
            break

        i += 1

    return i - index

def kwvar_fsm(string_input, index):
    i = index

    table = [
        [1,4,4,4],
        [4,2,4,4],
        [4,4,3,4],
        [4,4,4,4],
        [4,4,4,4],
    ]

    state = 0
    inputstate = 0

    string_length = len(string_input)

    while i != string_length:
        if string_input[i] == 'V':
            inputstate = 0
        elif string_input[i] == 'A':
            inputstate = 1
        elif string_input[i] == 'R':
            inputstate = 2
        else:
            inputstate = 3

        state = table[state][inputstate]

        if state == 4:
            break

        i += 1

    return i - index

def kwas_fsm(string_input, index):
    i = index

    table = [
        [1,3,3],
        [3,2,3],
        [3,3,3],
        [3,3,3],
    ]

    state = 0
    inputstate = 0

    string_length = len(string_input)

    while i != string_length:
        if string_input[i] == 'A':
            inputstate = 0
        elif string_input[i] == 'S':
            inputstate = 1
        else:
            inputstate = 2

        state = table[state][inputstate]

        if state == 3:
            break

        i += 1

    return i - index
