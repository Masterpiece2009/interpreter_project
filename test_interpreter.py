from interpreter.lexer import lexer
from interpreter.parser import parser
from interpreter.interpreter import Interpreter

def run_test(name, code, expected_output=None):
    print(f"\nRunning test: {name}")
    print("Code:")
    print(code)
    print("Output:")
    
    try:
        tokens = lexer.tokenize(code)
        ast = parser.parse(tokens)
        interpreter = Interpreter()
        result = interpreter.interpret(ast)
        if expected_output is not None and result != expected_output:
            print(f"Test failed: Expected {expected_output}, but got {result}")
            return False
        print("Test passed!")
        return True
    except Exception as e:
        print(f"Test failed: {str(e)}")
        return False

def main():
    tests = [
        # Basic arithmetic tests
        ("Addition", """
        x = 10;
        y = 5;
        print(x + y);
        """, 15.0),

        ("Subtraction", """
        x = 10;
        y = 5;
        print(x - y);
        """, 5.0),

        ("Multiplication", """
        x = 10;
        y = 5;
        print(x * y);
        """, 50.0),

        ("Division", """
        x = 10;
        y = 5;
        print(x / y);
        """, 2.0),

        # Comparison operators
        ("Greater Than", """
        print(10 > 5);
        """, True),

        ("Less Than", """
        print(10 < 5);
        """, False),

        ("Greater Than or Equal", """
        print(10 >= 5);
        """, True),

        ("Less Than or Equal", """
        print(10 <= 5);
        """, False),

        ("Equal To", """
        print(10 == 5);
        """, False),

        ("Not Equal To", """
        print(10 != 5);
        """, True),

        # Variable scoping
        ("Variable Assignment", """
        x = 10;
        print(x);
        """, 10.0),

        ("Variable Reassignment", """
        x = 5;
        x = x + 5;
        print(x);
        """, 10.0),

        # Functions
        ("Simple Function", """
        function add(a, b) {
            return a + b;
        }
        print(add(5, 3));
        """, 8.0),

        ("Recursive Function", """
        function factorial(n) {
            if (n <= 1) {
                return 1;
            }
            return n * factorial(n - 1);
        }
        print(factorial(5));
        """, 120.0),

        # Control flow
        ("If Statement", """
        x = 10;
        if (x > 5) {
            print(1);
        } else {
            print(0);
        }
        """, 1.0),

        ("While Loop", """
        x = 0;
        while (x < 5) {
            x = x + 1;
        }
        print(x);
        """, 5.0),

        # String operations
        ("String Concatenation", """
        print("Hello" + " World");
        """, "Hello World"),

        ("String Comparison", """
        print("Hello" == "Hello");
        """, True)
    ]

    passed = 0
    total = len(tests)

    for name, code, expected in tests:
        if run_test(name, code, expected):
            passed += 1

    print(f"\nTest Summary: {passed}/{total} tests passed")

if __name__ == "__main__":
    main() 