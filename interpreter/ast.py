class Node:
    def visit(self, env):
        raise NotImplementedError()

    def visit_statements(self, statements, env):
        result = None
        for statement in statements:
            result = statement.visit(env)
        return result

class Program(Node):
    def __init__(self, statements):
        self.statements = statements

class PrintStatement(Node):
    def __init__(self, expression):
        self.expression = expression

class Assignment(Node):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

class BinaryOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class UnaryOp(Node):
    def __init__(self, op, expression):
        self.op = op
        self.expression = expression

class Number(Node):
    def __init__(self, value):
        self.value = value

class String(Node):
    def __init__(self, value):
        self.value = value

class Boolean(Node):
    def __init__(self, value):
        self.value = value

class Variable(Node):
    def __init__(self, name):
        self.name = name

class IfStatement(Node):
    def __init__(self, condition, if_body, else_body=None):
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body

class WhileLoop(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class FunctionDef(Node):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FunctionCall(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class ReturnStatement(Node):
    def __init__(self, expression):
        self.expression = expression

class List(Node):
    def __init__(self, items):
        self.items = items

class ListAccess(Node):
    def __init__(self, list, index):
        self.list = list
        self.index = index 