from interpreter.lexer import lexer
from interpreter.parser import MyParser
from interpreter.interpreter import Interpreter

def main():
    # Example program
    program = """
    x = 5;
    y = 3;
    print(x + y);
    print(x - y);
    print(x * y);
    print(x / y);

    if (x > y) {
        print("x is greater than y");
    } else {
        print("x is not greater than y");
    }

    i = 0;
    while (i < 3) {
        print(i);
        i = i + 1;
    }

    function add(a, b) {
        return a + b;
    }
    print(add(5, 3));

    list = [1, 2, 3];
    print(list);
    list = append(list, 4);
    print(list);
    print(len(list));

    x = "42";
    print(type_of(x));
    y = to_number(x);
    print(type_of(y));
    print(y);

    write_file("test.txt", "Hello, World!");
    content = read_file("test.txt");
    print(content);
    append_file("test.txt", "\nAdditional line");
    content = read_file("test.txt");
    print(content);

    str1 = "Hello";
    str2 = "World";
    print(str1 + " " + str2);
    print(len(str1));

    x = true;
    y = false;
    print(x && y);
    print(x || y);
    print(!x);
    """

    try:
        # Tokenize
        tokens = lexer.tokenize(program)
        
        # Parse
        parser = MyParser()
        ast = parser.parse(tokens)
        
        # Interpret
        interpreter = Interpreter()
        interpreter.interpret(ast)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 