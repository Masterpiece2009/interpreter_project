class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class InterpreterError(Exception):
    def __init__(self, message, line_no=None):
        self.message = message
        self.line_no = line_no
        super().__init__(f"Line {line_no}: {message}" if line_no else message)

class TypeMismatchError(InterpreterError):
    pass

class Function:
    def __init__(self, name, params, body, env, interpreter):
        self.name = name
        self.params = params
        self.body = body
        self.env = env
        self.interpreter = interpreter

    def __call__(self, *args):
        if len(args) != len(self.params):
            raise InterpreterError(f"Function {self.name} expects {len(self.params)} arguments, got {len(args)}")
        
        # Create a new environment with the parent environment
        local_env = Environment(self.env)
        
        # Bind parameters to arguments in the new environment
        for param, arg in zip(self.params, args):
            local_env.set(param, arg)
        
        # Execute all statements
        last_value = None
        for stmt in self.body:
            try:
                last_value = self.interpreter.visit(stmt, local_env)
            except ReturnException as e:
                return e.value
        return last_value

class Environment:
    def __init__(self, parent=None):
        self.parent = parent
        self.variables = {}

    def get(self, name):
        if name in self.variables:
            return self.variables[name]
        if self.parent:
            return self.parent.get(name)
        raise NameError(f"Variable '{name}' is not defined")

    def set(self, name, value):
        # Always set in the current environment
        self.variables[name] = value

    def define(self, name, value):
        # Define a new variable in the current environment
        self.variables[name] = value

class Interpreter:
    def __init__(self):
        self.global_env = Environment()
        self.max_iterations = 1000
        self._setup_builtins()

    def _setup_builtins(self):
        builtins = {
            'print': lambda *args: print(*args),
            'input': lambda prompt='': input(prompt),
            'read_file': lambda path: open(path, 'r').read(),
            'write_file': lambda path, content: open(path, 'w').write(content),
            'append_file': lambda path, content: open(path, 'a').write(content),
            'type_of': lambda x: type(x).__name__,
            'to_string': lambda x: str(x),
            'to_number': lambda x: float(x) if '.' in str(x) else int(x),
            'len': lambda x: len(x),
            'append': lambda lst, item: lst + [item],
            'remove': lambda lst, item: [x for x in lst if x != item]
        }
        for name, func in builtins.items():
            self.global_env.set(name, func)

    def interpret(self, node):
        try:
            return self.visit(node, self.global_env)
        except ReturnException as e:
            return e.value

    def visit(self, node, env):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node, env)

    def generic_visit(self, node, env):
        raise InterpreterError(f'No visit_{type(node).__name__} method')

    def visit_Program(self, node, env):
        return self.visit_statements(node.statements, env)

    def visit_statements(self, statements, env):
        result = None
        for statement in statements:
            try:
                result = self.visit(statement, env)
            except InterpreterError as e:
                raise e
            except Exception as e:
                raise InterpreterError(f'Error executing statement: {str(e)}')
        return result

    def visit_PrintStatement(self, node, env):
        value = self.visit(node.expression, env)
        print(value)
        return value

    def visit_Assignment(self, node, env):
        value = self.visit(node.expression, env)
        env.set(node.name, value)
        return value

    def visit_BinaryOp(self, node, env):
        left = self.visit(node.left, env)
        right = self.visit(node.right, env)
        
        # Map token types to actual operators
        op_map = {
            'PLUS': '+',
            'MINUS': '-',
            'TIMES': '*',
            'DIVIDE': '/',
            'MOD': '%',
            'EQ': '==',
            'NE': '!=',
            'LT': '<',
            'GT': '>',
            'LE': '<=',
            'GE': '>=',
            'AND': '&&',
            'OR': '||'
        }
        
        op = op_map.get(node.op, node.op)
        
        if op == '+':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left + right
            elif isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            elif isinstance(left, list) and isinstance(right, list):
                return left + right
            else:
                raise TypeMismatchError(f"Cannot add {type(left)} and {type(right)}")
        elif op == '-':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left - right
            else:
                raise TypeMismatchError(f"Cannot subtract {type(right)} from {type(left)}")
        elif op == '*':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left * right
            else:
                raise TypeMismatchError(f"Cannot multiply {type(left)} and {type(right)}")
        elif op == '/':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                if right == 0:
                    raise InterpreterError("Division by zero")
                return left / right
            else:
                raise TypeMismatchError(f"Cannot divide {type(left)} by {type(right)}")
        elif op == '%':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                if right == 0:
                    raise InterpreterError("Modulo by zero")
                return left % right
            else:
                raise TypeMismatchError(f"Cannot perform modulo on {type(left)} and {type(right)}")
        elif op == '==':
            return bool(left == right)
        elif op == '!=':
            return bool(left != right)
        elif op == '<':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return bool(left < right)
            else:
                raise TypeMismatchError(f"Cannot compare {type(left)} and {type(right)} with <")
        elif op == '>':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return bool(left > right)
            else:
                raise TypeMismatchError(f"Cannot compare {type(left)} and {type(right)} with >")
        elif op == '<=':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return bool(left <= right)
            else:
                raise TypeMismatchError(f"Cannot compare {type(left)} and {type(right)} with <=")
        elif op == '>=':
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return bool(left >= right)
            else:
                raise TypeMismatchError(f"Cannot compare {type(left)} and {type(right)} with >=")
        elif op == '&&':
            if not isinstance(left, bool) or not isinstance(right, bool):
                raise TypeMismatchError(f"Cannot perform AND operation on {type(left)} and {type(right)}")
            return bool(left and right)
        elif op == '||':
            if not isinstance(left, bool) or not isinstance(right, bool):
                raise TypeMismatchError(f"Cannot perform OR operation on {type(left)} and {type(right)}")
            return bool(left or right)
        else:
            raise InterpreterError(f"Unknown operator: {op}")

    def visit_UnaryOp(self, node, env):
        expr = self.visit(node.expression, env)
        if node.op == 'NOT':
            if not isinstance(expr, bool):
                raise TypeMismatchError(f"Cannot perform NOT operation on {type(expr)}")
            return not expr
        elif node.op == '-':
            if isinstance(expr, (int, float)):
                return -expr
            else:
                raise TypeMismatchError(f"Cannot negate {type(expr)}")
        else:
            raise InterpreterError(f"Unknown unary operator: {node.op}")

    def visit_Number(self, node, env):
        return node.value

    def visit_String(self, node, env):
        return node.value

    def visit_Boolean(self, node, env):
        return node.value

    def visit_Variable(self, node, env):
        return env.get(node.name)

    def visit_IfStatement(self, node, env):
        condition = self.visit(node.condition, env)
        if condition:
            for stmt in node.if_body:
                try:
                    result = self.visit(stmt, env)
                except ReturnException as e:
                    raise e
            return result
        elif node.else_body:
            for stmt in node.else_body:
                try:
                    result = self.visit(stmt, env)
                except ReturnException as e:
                    raise e
            return result
        return None

    def visit_WhileLoop(self, node, env):
        iterations = 0
        while self.visit(node.condition, env):
            if iterations >= self.max_iterations:
                raise InterpreterError("Maximum iteration limit reached")
            self.visit_statements(node.body, env)
            iterations += 1
        return None

    def visit_FunctionDef(self, node, env):
        # Create function object and store it in the current environment
        func = Function(node.name, node.params, node.body, env, self)
        env.define(node.name, func)
        return func

    def visit_FunctionCall(self, node, env):
        # Get the function from the environment
        func = env.get(node.name)
        if not callable(func):
            raise InterpreterError(f"{node.name} is not a function")
        
        # Evaluate arguments in the current environment
        args = [self.visit(arg, env) for arg in node.args]
        
        try:
            # Call the function with evaluated arguments
            return func(*args)
        except Exception as e:
            if isinstance(e, ReturnException):
                return e.value
            raise InterpreterError(f"Error calling function {node.name}: {str(e)}")

    def visit_ReturnStatement(self, node, env):
        value = self.visit(node.expression, env) if node.expression else None
        raise ReturnException(value)

    def visit_List(self, node, env):
        return [self.visit(item, env) for item in node.items]

    def visit_ListAccess(self, node, env):
        lst = self.visit(node.list, env)
        index = self.visit(node.index, env)
        if not isinstance(lst, list):
            raise TypeMismatchError(f"Cannot index into {type(lst)}")
        if isinstance(index, float):
            if not index.is_integer():
                raise TypeMismatchError(f"List index must be an integer, got float {index}")
            index = int(index)
        if not isinstance(index, int):
            raise TypeMismatchError(f"List index must be an integer, got {type(index)}")
        if index < 0 or index >= len(lst):
            raise InterpreterError(f"List index out of range: {index}")
        return lst[index] 