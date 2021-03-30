from re import match
from finite_state_machines import data_types, identifier, logical_operator, operator, keywords
import Tokens


class Lexer:

    op_dict = {
        '+': Tokens.PLUS,
        '-': Tokens.MINUS,
        '*': Tokens.MULTIPLY,
        '/': Tokens.DIVIDE,
        '%': Tokens.MODULO,
        '&': Tokens.CONCATENATOR,
        '(': Tokens.PAREN_OPEN,
        ')': Tokens.PAREN_CLOSE,
        '>': Tokens.GREATER_THAN,
        '<': Tokens.LESS_THAN,
        '>=': Tokens.GREATER_OR_EQUAL,
        '<=': Tokens.LESS_OR_EQUAL,
        '=': Tokens.EQUALS,
        '==': Tokens.LOGIC_EQUAL,
        '<>': Tokens.NOT_EQUAL,
        '&&': Tokens.AND,
        '||': Tokens.OR,
    }

    def lexicalize(self, statement):

        token_stream = list()
        index = 0
        stmt_length = len(statement)

        while index < stmt_length:

            if statement[index] == ' ':
                index += 1
                continue

            match_dict = dict()

            # keyword match counts
            start_count = keywords.kwstart_fsm(statement, index)
            match_dict[Tokens.KW_START] = start_count
            stop_count = keywords.kwstop_fsm(statement, index)
            match_dict[Tokens.KW_STOP] = stop_count
            var_count = keywords.kwvar_fsm(statement, index)
            match_dict[Tokens.KW_VAR] = var_count
            as_count = keywords.kwas_fsm(statement, index)
            match_dict[Tokens.KW_AS] = as_count
            kw_int_count = keywords.kwinteger_fsm(statement, index)
            match_dict[Tokens.KW_INT] = kw_int_count
            kw_float_count = keywords.kwfloat_fsm(statement, index)
            match_dict[Tokens.KW_FLOAT] = kw_float_count
            kw_str_count = keywords.kwstring_fsm(statement, index)
            match_dict[Tokens.KW_STRING] = kw_str_count
            kw_bool_count = keywords.kwboolean_fsm(statement, index)
            match_dict[Tokens.KW_BOOLEAN] = kw_bool_count
            kw_output_count = keywords.kwoutput_fsm(statement, index)
            match_dict[Tokens.KW_OUTPUT] = kw_output_count
            kw_input_count = keywords.kwinput_fsm(statement, index)
            match_dict[Tokens.KW_INPUT] = kw_input_count
            kw_char_count = keywords.kwchar_fsm(statement, index)
            match_dict[Tokens.KW_CHAR] = kw_char_count
            comma_count = keywords.kwcomma_fsm(statement, index)
            match_dict[Tokens.COMMA] = comma_count
            colon_count = keywords.kwcolon_fsm(statement, index)
            match_dict[Tokens.COLON] = colon_count

            # operator
            operator_count = operator.operator_fsm(statement, index)  # includes concat(&) operator
            match_dict['Operator'] = operator_count
            logic_op_count = logical_operator.logicalop_fsm(statement, index)
            match_dict['LogicOp'] = logic_op_count

            # data types match counts
            int_count = data_types.int_lexer(statement, index)
            match_dict[Tokens.INT] = int_count
            float_count = data_types.float_lexer(statement, index)
            match_dict[Tokens.FLOAT] = float_count
            unary_int_count = data_types.intUnary_lexer(statement, index)
            match_dict[Tokens.UNARY_INT] = unary_int_count
            unary_float_count = data_types.floatUnary_lexer(statement, index)
            match_dict[Tokens.UNARY_FLOAT] = unary_float_count
            char_count = data_types.char_lexer(statement, index)
            match_dict[Tokens.CHAR] = char_count
            string_count = data_types.string_lexer(statement, index)
            match_dict[Tokens.STRING] = string_count
            true_bool_count = data_types.true_bool_lexer(statement, index)
            match_dict[Tokens.BOOL_TRUE] = true_bool_count
            false_bool_count = data_types.false_bool_lexer(statement, index)
            match_dict[Tokens.BOOL_FALSE] = false_bool_count

            # identifier
            iden_count = identifier.iden_fsm(statement, index)
            match_dict[Tokens.IDENTIFIER] = iden_count

            longest_match = max(match_dict.values())

            if longest_match == 0:
                # if lexer sees an unidentified character
                token_stream.append([Tokens.ERROR, statement[index]])
                index += 1
                continue

            token_type = self.get_key(match_dict, longest_match)

            match_string = statement[index:index+longest_match]

            if token_type == Tokens.STRING:
                if longest_match == 1 or not (match_string.startswith('"') and match_string.endswith('"')):
                    token_stream.append([Tokens.ERROR, match_string])
                    index += longest_match
                    continue

            if token_type in ('LogicOp', 'Operator'):
                token_type = self.op_dict[match_string]

            if token_type in (Tokens.UNARY_FLOAT, Tokens.UNARY_INT):
                if token_stream and token_stream[-1][0] in (Tokens.IDENTIFIER, Tokens.INT, Tokens.FLOAT):
                    token_stream.append([Tokens.PLUS, '+'])
                token_type = Tokens.FLOAT if token_type == Tokens.UNARY_FLOAT else Tokens.INT

            token_stream.append([token_type, match_string])
            index += longest_match

        # for key, value in match_dict.items():
        #    print(f'{key} : {value}')

        return token_stream

    def get_key(self, my_dict, value):
        for key, count in my_dict.items():
            if value == count:
                return key
        return 'key doesn\'t exist.'
