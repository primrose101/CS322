import Tokens


class Parser:

    def parse(self, token_stream):

        if len(token_stream) == 1:
            if token_stream[0][0] == Tokens.KW_START:
                return Tokens.ST_START
            elif token_stream[0][0] == Tokens.KW_STOP:
                return Tokens.ST_STOP

        stmnt = self.assignmentTree(token_stream)

        if stmnt == Tokens.ERROR:
            stmnt = self.outfut(token_stream)

        if stmnt == Tokens.ERROR:
            stmnt = self.inpout(token_stream)

        if stmnt == Tokens.ERROR:
            stmnt = self.declaration(token_stream)

        return stmnt

    def assignmentTree(self, token_stream):
        assZZ = self.string_assignment(token_stream)

        if assZZ == Tokens.ERROR:
            assZZ = self.math_assignment(token_stream)

        if assZZ == Tokens.ERROR:
            assZZ = self.logic_assignment(token_stream)

        return assZZ

    def string_assignment(self, token_stream):
        stateTable = [[1, 4, 4, 4],
                      [4, 2, 4, 4],
                      [3, 4, 3, 4],
                      [4, 4, 4, 2],
                      [4, 4, 4, 4]]
        state = 0
        infut = 0

        for token in token_stream:
            if token[0] == Tokens.IDENTIFIER:
                infut = 0
            elif token[0] == Tokens.EQUALS:
                infut = 1
            elif token[0] == Tokens.STRING:
                infut = 2
            elif token[0] == Tokens.CHAR:
                infut = 2
            elif token[0] == Tokens.CONCATENATOR:
                infut = 3

            state = stateTable[state][infut]
            if state == 4:
                break

        if state == 3:
            return Tokens.ST_ASSIGNMENT_STRING
        else:
            return Tokens.ERROR

    def math_assignment(self, token_stream):
        stateTable = [[1, 4, 4, 4, 4, 4],
                      [4, 2, 4, 4, 4, 4],
                      [3, 4, 3, 4, 2, 4],
                      [4, 4, 4, 2, 4, 3],
                      [4, 4, 4, 4, 4, 4]]
        state = 0
        infut = 0

        for token in token_stream:
            if token[0] == Tokens.IDENTIFIER:
                infut = 0
            elif token[0] == Tokens.EQUALS:
                infut = 1
            elif token[0] == Tokens.INT:
                infut = 2
            elif token[0] == Tokens.FLOAT:
                infut = 2
            elif token[0] == Tokens.MULTIPLY:
                infut = 3
            elif token[0] == Tokens.DIVIDE:
                infut = 3
            elif token[0] == Tokens.PLUS:
                infut = 3
            elif token[0] == Tokens.MINUS:
                infut = 3
            elif token[0] == Tokens.MODULO:
                infut = 3
            elif token[0] == Tokens.PAREN_OPEN:
                infut = 4
            elif token[0] == Tokens.PAREN_CLOSE:
                infut = 5

            state = stateTable[state][infut]
            if state == 4:
                break

        if state == 3:
            return Tokens.ST_ASSIGNMENT_MATH
        else:
            return Tokens.ERROR

    def logic_assignment(self, token_stream):
        stateTable = [[1, 4, 4, 4],
                      [4, 2, 4, 4],
                      [3, 4, 3, 4],
                      [4, 4, 4, 2],
                      [4, 4, 4, 4]]
        state = 0
        infut = 0

        for token in token_stream:
            if token[0] == Tokens.IDENTIFIER:
                infut = 0
            elif token[0] == Tokens.EQUALS:
                infut = 1
            elif token[0] == Tokens.BOOL_TRUE:
                infut = 2
            elif token[0] == Tokens.BOOL_FALSE:
                infut = 2
            elif token[0] == Tokens.AND:
                infut = 3
            elif token[0] == Tokens.OR:
                infut = 3
            elif token[0] == Tokens.GREATER_OR_EQUAL:
                infut = 3
            elif token[0] == Tokens.GREATER_THAN:
                infut = 3
            elif token[0] == Tokens.LESS_OR_EQUAL:
                infut = 3
            elif token[0] == Tokens.LESS_THAN:
                infut = 3
            elif token[0] == Tokens.LOGIC_EQUAL:
                infut = 3
            elif token[0] == Tokens.NOT_EQUAL:
                infut = 3

            state = stateTable[state][infut]
            if state == 4:
                break

        if state == 3:
            return Tokens.ST_ASSIGNMENT_LOGIC
        else:
            return Tokens.ERROR

    def outfut(self, token_stream):
        stateTable = [[1, 4, 4, 4, 4, 4],
                      [4, 2, 4, 4, 4, 4],
                      [4, 4, 3, 4, 4, 3],
                      [4, 4, 4, 2, 2, 4],
                      [4, 4, 4, 4, 4, 4]]
        state = 0
        infut = 0

        for token in token_stream:
            if token[0] == Tokens.KW_OUTPUT:
                infut = 0
            elif token[0] == Tokens.COLON:
                infut = 1
            elif token[0] == Tokens.IDENTIFIER:
                infut = 2
            elif token[0] == Tokens.STRING:
                infut = 2
            elif token[0] == Tokens.COMMA:
                infut = 3
            elif token[0] == Tokens.CONCATENATOR:
                infut = 3
            else:
                infut = 4

            state = stateTable[state][infut]
            if state == 4:
                break

        if state == 3:
            return Tokens.ST_OUTPUT
        else:
            return Tokens.ERROR

    def inpout(self, token_stream):
        stateTable = [[1, 4, 4, 4],
                      [4, 2, 4, 4],
                      [4, 4, 3, 4],
                      [4, 4, 4, 2],
                      [4, 4, 4, 4]]
        state = 0
        infut = 0

        for token in token_stream:
            if token[0] == Tokens.KW_INPUT:
                infut = 0
            elif token[0] == Tokens.COLON:
                infut = 1
            elif token[0] == Tokens.IDENTIFIER:
                infut = 2
            elif token[0] == Tokens.COMMA:
                infut = 3

            state = stateTable[state][infut]
            if state == 4:
                break

        if state == 3:
            return Tokens.ST_INPUT
        else:
            return Tokens.ERROR

    def declaration(self, token_stream):
        stateTable = [[1, 7, 7, 7, 7, 7, 7],
                      [7, 2, 7, 7, 7, 7, 7],
                      [7, 7, 1, 5, 7, 3, 7],
                      [7, 7, 7, 7, 7, 7, 4],
                      [7, 7, 7, 7, 7, 7, 7],
                      [7, 7, 7, 7, 6, 7, 7],
                      [7, 7, 1, 7, 7, 3, 7],
                      [7, 7, 7, 7, 7, 7, 7]]
        state = 0
        infut = 0

        for token in token_stream:
            if token[0] == Tokens.KW_VAR:
                infut = 0
            elif token[0] == Tokens.IDENTIFIER:
                infut = 1
            elif token[0] == Tokens.COMMA:
                infut = 2
            elif token[0] == Tokens.EQUALS:
                infut = 3
            elif token[0] in (Tokens.INT, Tokens.FLOAT, Tokens.STRING, Tokens.CHAR, Tokens.BOOL_TRUE, Tokens.BOOL_FALSE):
                infut = 4
            elif token[0] == Tokens.KW_AS:
                infut = 5
            elif token[0] in (Tokens.KW_INT, Tokens.KW_FLOAT, Tokens.KW_STRING, Tokens.KW_CHAR, Tokens.KW_BOOLEAN):
                infut = 6

            state = stateTable[state][infut]

            if state == 7:
                break

        if state == 4:
            return Tokens.ST_DECLARATION
        else:
            return Tokens.ERROR
