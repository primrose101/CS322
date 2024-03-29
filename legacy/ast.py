class AST:
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right
        self.value = None


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Char(Num):
    pass


class Bool(Num):
    pass


class String(Num):
    pass


class Input(Num):
    pass


class Output(Num):
    pass


class IfStatement(AST):
    def __init__(self, token, expr, els=None):
        self.token = token
        self.value = token.value
        self.expr = expr
        self.els = els


class WhileStatement(AST):
    def __init__(self, token, expr):
        self.token = token
        self.value = token.value
        self.expr = expr


class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr


class Compound(AST):
    """Represents a 'START ... STOP' block"""

    def __init__(self):
        self.children = []


class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class Var(AST):
    """The Var node is constructed out of ID token."""

    def __init__(self, token):
        self.token = token
        self.value = token.value
        self.default_value = None


class NoOp(AST):
    pass


class Program(AST):
    def __init__(self, block):
        self.block = block


class Block(AST):
    def __init__(self, declarations, compound_statement):
        self.declarations = declarations
        self.compound_statement = compound_statement


class VarDecl(AST):
    def __init__(self, var_node, type_node):
        self.var_node = var_node
        self.type_node = type_node


class Type(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
