from sly import Lexer

class MyLexer(Lexer):
    # Define all token names
    tokens = {
        'NUMBER', 'STRING', 'IDENTIFIER',
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
        'EQ', 'NE', 'LT', 'LE', 'GT', 'GE',
        'AND', 'OR', 'NOT',
        'ASSIGN',
        'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
        'LBRACKET', 'RBRACKET',
        'SEMICOLON', 'COMMA',
        'IF', 'ELSE', 'WHILE', 'FUNCTION', 'RETURN', 'PRINT',
        'TRUE', 'FALSE'
    }

    # String containing ignored characters
    ignore = ' \t'
    ignore_comment = r'(//.*|#.*)'
    ignore_newline = r'\n+'

    # Regular expression rules for tokens
    # Operators
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    MOD = r'%'

    # Comparison operators
    EQ = r'=='
    NE = r'!='
    LE = r'<='
    GE = r'>='
    LT = r'<'
    GT = r'>'

    # Boolean operators
    AND = r'&&'
    OR = r'\|\|'
    NOT = r'!'

    # Delimiters
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACE = r'\{'
    RBRACE = r'\}'
    LBRACKET = r'\['
    RBRACKET = r'\]'
    SEMICOLON = r';'
    COMMA = r','
    ASSIGN = r'='

    # Keywords
    FUNCTION = r'function'
    IF = r'if'
    ELSE = r'else'
    WHILE = r'while'
    RETURN = r'return'
    PRINT = r'print'
    TRUE = r'true'
    FALSE = r'false'

    @_(r'\d+(\.\d+)?')
    def NUMBER(self, t):
        t.value = float(t.value)
        return t

    @_(r'"[^"]*"')
    def STRING(self, t):
        t.value = t.value[1:-1]
        return t

    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def IDENTIFIER(self, t):
        # Check if it's a keyword
        if t.value in {'if', 'else', 'while', 'function', 'return', 'print', 'true', 'false'}:
            t.type = t.value.upper()
        return t

    def error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        self.index += 1

# Create a global lexer instance
lexer = MyLexer() 