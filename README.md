# Python Interpreter Project

A simple but powerful interpreter implemented in Python that supports various programming constructs including arithmetic operations, control flow, functions, and more. This project demonstrates the implementation of a basic programming language interpreter from scratch.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Language Syntax](#language-syntax)
- [Examples](#examples)
- [Implementation Details](#implementation-details)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Dependencies](#dependencies)


## Features

### Basic Operations
- **Arithmetic Operations**
  - Addition: `+`
  - Subtraction: `-`
  - Multiplication: `*`
  - Division: `/`
  - Modulo: `%`
  - Unary minus: `-`

- **Comparison Operators**
  - Equal: `==`
  - Not equal: `!=`
  - Less than: `<`
  - Greater than: `>`
  - Less than or equal: `<=`
  - Greater than or equal: `>=`

- **Boolean Operations**
  - AND: `&&`
  - OR: `||`
  - NOT: `!`

- **String Operations**
  - Concatenation: `+`
  - Length: `len()`

- **List Operations**
  - Creation: `[1, 2, 3]`
  - Indexing: `list[0]`
  - Append: `append(list, item)`
  - Remove: `remove(list, item)`
  - Length: `len(list)`

### Control Flow
- **If-Else Statements**
  ```python
  if (condition) {
      // statements
  } else {
      // statements
  }
  ```

- **While Loops**
  ```python
  while (condition) {
      // statements
  }
  ```

- **Functions**
  ```python
  function name(param1, param2) {
      // statements
      return value;
  }
  ```

### Data Types
- **Numbers**
  - Integers: `42`
  - Floats: `3.14`

- **Strings**
  - Single line: `"Hello"`
  - Concatenation: `"Hello" + "World"`

- **Booleans**
  - `true`
  - `false`

- **Lists**
  - Creation: `[1, 2, 3]`
  - Access: `list[0]`

### Built-in Functions
- **I/O Operations**
  - `print(value)`: Output to console
  - `input(prompt)`: Get user input
  - `read_file(path)`: Read file contents
  - `write_file(path, content)`: Write to file
  - `append_file(path, content)`: Append to file

- **Type Operations**
  - `type_of(value)`: Get type of value
  - `to_string(value)`: Convert to string
  - `to_number(value)`: Convert to number

- **List Operations**
  - `len(list)`: Get length
  - `append(list, item)`: Add item
  - `remove(list, item)`: Remove item

## Project Structure

```
interpreter_project/
├── interpreter/
│   ├── __init__.py
│   ├── lexer.py      # Tokenizes input code
│   ├── parser.py     # Parses tokens into AST
│   ├── interpreter.py # Executes AST
│   ├── ast.py        # Abstract Syntax Tree definitions
│   └── main.py       # Main entry point
├── test_interpreter.py  # Test suite
├── run.py            # Script to run the interpreter
└── requirements.txt   # Project dependencies
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the interpreter:
```bash
python run.py
```

2. Run tests:
```bash
python test_interpreter.py
```

## Language Syntax

### Comments
```python
// Single line comment
# Also single line comment
```

### Variables
```python
x = 42;
name = "John";
list = [1, 2, 3];
```

### Control Flow
```python
if (x > 0) {
    print("Positive");
} else {
    print("Non-positive");
}

while (i < 10) {
    print(i);
    i = i + 1;
}
```

### Functions
```python
function add(a, b) {
    return a + b;
}

function factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

## Examples

### Basic Arithmetic
```python
x = 10;
y = 5;
print(x + y);  // 15
print(x - y);  // 5
print(x * y);  // 50
print(x / y);  // 2
```

### String Operations
```python
name = "World";
print("Hello, " + name + "!");  // Hello, World!
```

### List Operations
```python
numbers = [1, 2, 3];
print(numbers);     // [1, 2, 3]
print(numbers[0]);  // 1
numbers = append(numbers, 4);
print(numbers);     // [1, 2, 3, 4]
```

### File Operations
```python
write_file("test.txt", "Hello");
append_file("test.txt", " World");
content = read_file("test.txt");
print(content);  // Hello World
```

## Implementation Details

### Lexer
- Tokenizes input code into tokens
- Handles numbers, strings, identifiers, and operators
- Supports comments (both `//` and `#`)
- Implements error handling for illegal characters

### Parser
- Converts tokens into an Abstract Syntax Tree (AST)
- Implements operator precedence
- Handles nested structures
- Supports function definitions and calls
- Uses SLY for lexing and parsing

### Interpreter
- Executes the AST
- Manages variable scoping with Environment class
- Handles function calls and returns
- Implements built-in functions
- Provides error handling

### AST
- Defines node types for different language constructs
- Includes nodes for expressions, statements, and declarations
- Supports binary and unary operations
- Handles control flow structures

## Error Handling

The interpreter provides detailed error messages for:
- Syntax errors
- Type mismatches
- Undefined variables
- Division by zero
- Invalid list indices
- Function argument count mismatches

## Testing

The project includes a comprehensive test suite that verifies:
- Basic arithmetic operations
- Comparison operators
- Boolean operations
- String operations
- Control flow statements
- Function definitions and calls
- List operations
- Error handling

Run tests with:
```bash
python test_interpreter.py
```

## Dependencies

- sly: Lexer and parser generator
- Python 3.x

