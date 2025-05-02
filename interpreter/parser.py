from interpreter.ast import *
from interpreter.lexer import lexer
from sly import Parser

class MyParser(Parser):
    tokens = lexer.tokens

    # Define precedence and associativity rules
    precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('nonassoc', 'EQ', 'NE'),
        ('nonassoc', 'LT', 'GT', 'LE', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE', 'MOD'),
        ('right', 'NOT', 'UMINUS'),
        ('left', 'LBRACKET'),  # Array indexing
        ('left', 'LPAREN'),  # Function calls
    )

    def __init__(self):
        super().__init__()
        self.env = {}

    @_('statements')
    def program(self, p):
        return Program(p.statements)

    @_('statement statements')
    def statements(self, p):
        return [p.statement] + p.statements

    @_('')
    def statements(self, p):
        return []

    @_('PRINT expression SEMICOLON')
    def statement(self, p):
        return PrintStatement(p.expression)

    @_('RETURN expression SEMICOLON')
    def statement(self, p):
        return ReturnStatement(p.expression)

    @_('RETURN SEMICOLON')
    def statement(self, p):
        return ReturnStatement(None)

    @_('IDENTIFIER ASSIGN expression SEMICOLON')
    def statement(self, p):
        return Assignment(p.IDENTIFIER, p.expression)

    @_('IF LPAREN expression RPAREN LBRACE statements RBRACE')
    def statement(self, p):
        return IfStatement(p.expression, p.statements, None)

    @_('IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE')
    def statement(self, p):
        return IfStatement(p.expression, p.statements0, p.statements1)

    @_('IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE if_statement')
    def statement(self, p):
        return IfStatement(p.expression, p.statements, [p.if_statement])

    @_('IF LPAREN expression RPAREN LBRACE statements RBRACE')
    def if_statement(self, p):
        return IfStatement(p.expression, p.statements, None)

    @_('IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE')
    def if_statement(self, p):
        return IfStatement(p.expression, p.statements0, p.statements1)

    @_('IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE if_statement')
    def if_statement(self, p):
        return IfStatement(p.expression, p.statements, [p.if_statement])

    @_('WHILE LPAREN expression RPAREN LBRACE statements RBRACE')
    def statement(self, p):
        return WhileLoop(p.expression, p.statements)

    @_('FUNCTION IDENTIFIER LPAREN params RPAREN LBRACE statements RBRACE')
    def statement(self, p):
        return FunctionDef(p.IDENTIFIER, p.params, p.statements)

    @_('expression SEMICOLON')
    def statement(self, p):
        return p.expression

    @_('IDENTIFIER')
    def params(self, p):
        return [p.IDENTIFIER]

    @_('IDENTIFIER COMMA params')
    def params(self, p):
        return [p.IDENTIFIER] + p.params

    @_('')
    def params(self, p):
        return []

    @_('expression')
    def args(self, p):
        return [p.expression]

    @_('expression COMMA args')
    def args(self, p):
        return [p.expression] + p.args

    @_('')
    def args(self, p):
        return []

    @_('term')
    def expression(self, p):
        return p.term

    @_('expression PLUS term',
       'expression MINUS term',
       'expression TIMES term',
       'expression DIVIDE term',
       'expression MOD term')
    def expression(self, p):
        return BinaryOp(p.expression, p[1], p.term)

    @_('expression EQ term',
       'expression NE term',
       'expression LT term',
       'expression GT term',
       'expression LE term',
       'expression GE term')
    def expression(self, p):
        return BinaryOp(p.expression, p[1], p.term)

    @_('expression AND term',
       'expression OR term')
    def expression(self, p):
        return BinaryOp(p.expression, p[1], p.term)

    @_('NOT term')
    def expression(self, p):
        return UnaryOp('NOT', p.term)

    @_('MINUS term %prec UMINUS')
    def expression(self, p):
        return UnaryOp('-', p.term)

    @_('NUMBER')
    def term(self, p):
        return Number(p.NUMBER)

    @_('STRING')
    def term(self, p):
        return String(p.STRING)

    @_('TRUE')
    def term(self, p):
        return Boolean(True)

    @_('FALSE')
    def term(self, p):
        return Boolean(False)

    @_('IDENTIFIER')
    def term(self, p):
        return Variable(p.IDENTIFIER)

    @_('LPAREN expression RPAREN')
    def term(self, p):
        return p.expression

    @_('LBRACKET items RBRACKET')
    def term(self, p):
        return List(p.items)

    @_('term LBRACKET expression RBRACKET')
    def term(self, p):
        return ListAccess(p.term, p.expression)

    @_('IDENTIFIER LPAREN args RPAREN')
    def term(self, p):
        return FunctionCall(p.IDENTIFIER, p.args)

    @_('IDENTIFIER LPAREN RPAREN')
    def term(self, p):
        return FunctionCall(p.IDENTIFIER, [])

    @_('expression')
    def items(self, p):
        return [p.expression]

    @_('expression COMMA items')
    def items(self, p):
        return [p.expression] + p.items

    @_('')
    def items(self, p):
        return []

    def error(self, p):
        if p:
            raise SyntaxError(f"Syntax error at token {p.type}")
        else:
            raise SyntaxError("Syntax error at EOF")

# Create a global parser instance
parser = MyParser() 