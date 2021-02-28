import Tokens


class Parser:
    
    def assignment(self,token_stream):
        stateTable = [[1,4,4,4],
                      [4,2,4,4],
                      [3,4,3,4],
                      [4,4,4,2],
                      [4,4,4,4]]
        state = 0
        infut = 0

        for token in token_stream:
            if token == Tokens.IDENTIFIER:
                infut = 0
            elif token == Tokens.EQUALS:
                infut = 1
            elif token == Tokens.STRING:
                infut = 2
            elif token == Tokens.CHAR:
                infut = 2
            elif token == Tokens.INT:
                infut = 2
            elif token == Tokens.FLOAT:
                infut = 2
            elif token == Tokens.BOOL_FALSE:
                infut = 2
            elif token == Tokens.BOOL_TRUE:
                infut = 2
            elif token == Tokens.MULTIPLY:
                infut = 3
            elif token == Tokens.DIVIDE:
                infut = 3
            elif token == Tokens.PLUS:
                infut = 3
            elif token == Tokens.MINUS:
                infut = 3
            elif token == Tokens.MODULO:
                infut = 3

            state = stateTable[state][infut]
            if state == 4:
                break

        
        if state == 3:
            return Tokens.ST_ASSIGNMENT
        else:
            return Tokens.ERROR

        
    def outfut(self,token_stream):
        stateTable = [[1,4,4,4],
                      [4,2,4,4],
                      [3,4,3,4],
                      [4,4,4,2],
                      [4,4,4,4]]
        state = 0
        infut = 0

        for token in token_stream:
            if token == Tokens.KW_OUTPUT:
                infut = 0
            elif token == ':':
                infut = 1
            elif token == Tokens.STRING:
                infut = 2
            elif token == Tokens.CHAR:
                infut = 2
            elif token == Tokens.INT:
                infut = 2
            elif token == Tokens.FLOAT:
                infut = 2
            elif token == Tokens.BOOL_FALSE:
                infut = 2
            elif token == Tokens.BOOL_TRUE:
                infut = 2
            elif token == Tokens.MULTIPLY:
                infut = 3
            elif token == Tokens.DIVIDE:
                infut = 3
            elif token == Tokens.PLUS:
                infut = 3
            elif token == Tokens.MINUS:
                infut = 3
            elif token == Tokens.MODULO:
                infut = 3

            state = stateTable[state][infut]
            if state == 4:
                break
        
        if state == 3:
            return Tokens.ST_OUTPUT
        else:
            return Tokens.ERROR
        
    def inpout(self,token_stream):
        stateTable = [[1,5,5,5],
                      [5,2,5,5],
                      [5,5,3,5],
                      [5,5,5,4],
                      [5,5,3,5],
                      [5,5,5,5]]
        state = 0
        infut = 0

        for token in token_stream:
            if token == Tokens.KW_OUTPUT:
                infut = 0
            elif token == ':':
                infut = 1
            elif token == Tokens.STRING:
                infut = 2
            elif token == Tokens.CHAR:
                infut = 2
            elif token == Tokens.INT:
                infut = 2
            elif token == Tokens.FLOAT:
                infut = 2
            elif token == Tokens.BOOL_FALSE:
                infut = 2
            elif token == Tokens.BOOL_TRUE:
                infut = 2
            elif token == Tokens.MULTIPLY:
                infut = 3
            elif token == Tokens.DIVIDE:
                infut = 3
            elif token == Tokens.PLUS:
                infut = 3
            elif token == Tokens.MINUS:
                infut = 3
            elif token == Tokens.MODULO:
                infut = 3

            state = stateTable[state][infut]
            if state == 4:
                break
        
        if state == 3:
            return "INPUT"
        else:
            return Tokens.ERROR
        

    def declaration(self,token_stream):
        stateTable = [[1,7,7,7,7,7,7],
                      [7,2,7,7,7,7,7],
                      [7,7,1,3,7,5,7],
                      [7,7,7,7,4,7,7],
                      [7,7,7,7,7,7,7],
                      [7,7,7,7,7,7,7],
                      [7,7,1,7,7,7,7],
                      [7,7,7,7,7,7,7]]
        state = 0
        infut = 0

        for token in token_stream:
            if token == Tokens.KW_VAR:
                infut = 0
            elif token == Tokens.IDENTIFIER:
                infut = 1
            elif token == Tokens.COMMA:
                infut = 2
            elif token == Tokens.KW_AS:
                infut = 3
            elif token == Tokens.KW_INT:
                infut = 4
            elif token == Tokens.KW_FLOAT:
                infut = 4
            elif token == Tokens.KW_STRING:
                infut = 4
            elif token == Tokens.KW_BOOLEAN:
                infut = 4
            elif token == Tokens.EQUALS:
                infut = 5
            elif token == Tokens.STRING:
                infut = 6
            elif token == Tokens.CHAR:
                infut = 6
            elif token == Tokens.INT:
                infut = 6
            elif token == Tokens.FLOAT:
                infut = 3
            elif token == Tokens.BOOL_FALSE:
                infut = 6
            elif token == Tokens.BOOL_TRUE:
                infut = 6

            state = stateTable[state][infut]

            if state == 7:
                break

        
        if state == 4 or state == 6:
            return Tokens.ST_DECLARATION
        else:
            return Tokens.ERROR
        