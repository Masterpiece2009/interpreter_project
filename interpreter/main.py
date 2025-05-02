from interpreter.lexer import lexer
from interpreter.parser import parser
from interpreter.interpreter import Interpreter

def run_program(program):
    try:
        # Tokenize the input using the lexer
        tokens = lexer.tokenize(program)
        
        # Parse the tokens into an AST
        ast = parser.parse(tokens)
        
        # Interpret the AST
        interpreter = Interpreter()
        result = interpreter.interpret(ast)
        
        return result
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    # Test program
    program = """
    // Arithmetic operations
    print(10 + 5);  // 15
    print(10 - 5);  // 5
    print(10 * 5);  // 50
    print(10 / 5);  // 2

    // Comparison operations
    print(10 > 5);   // true
    print(10 < 5);   // false
    print(10 >= 5);  // true
    print(10 <= 5);  // false
    print(10 == 5);  // false
    print(10 != 5);  // true

    // Boolean operations
    print(true && true);   // true
    print(true && false);  // false
    print(true || false);  // true
    print(false || false); // false
    print(!true);         // false
    print(!false);        // true

    // String operations
    print("Hello" + " " + "World");  // Hello World

    // Variable assignments
    x = 42;
    print(x);             // 42
    y = "test";
    print(y);             // test
    z = true;
    print(z);             // true

    // List operations
    list = [1, 2, 3];
    print(list);          // [1, 2, 3]
    print(list[0]);       // 1
    print(list[1]);       // 2
    print(list[2]);       // 3

    // Control flow
    if (x > 40) {
        print("x is greater than 40");
    } else {
        print("x is less than or equal to 40");
    }

    // Loop
    i = 0;
    while (i < 3) {
        print(i);
        i = i + 1;
    }
    """

    run_program(program)

if __name__ == "__main__":
    main() 