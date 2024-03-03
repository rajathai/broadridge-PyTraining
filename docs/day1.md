# Day 01

## **Introduction to Python**

![Python](assets/images/python-logo.png){ align=left width=150 }
<p style="text-align: justify;">Python is a high-level, interpreted programming language known for its clear syntax and readability. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.</p>

<p style="text-align: justify;">Its versatile nature allows Python to be used in various domains, such as web development, data analysis, artificial intelligence, machine learning, automation, and scientific computing. Companies like Google, Netflix, and Facebook use Python for a wide range of purposes, demonstrating its adaptability and power.</p>

<p style="text-align: justify;">With a rich ecosystem of libraries and frameworks, Python makes it possible to work on complex tasks with relatively simple and understandable code, making it a popular choice for beginners and experts alike.</p>

## **Features of Python**

Python is known for its numerous appealing features which contribute to its popularity among programmers. Below are some of the most notable features:

- **Ease of Learning and Readability**: Python's syntax is clear and intuitive, making it an ideal choice for beginners.
- **Expressive**: More functionality can be achieved with fewer lines of code.
- **Interpreted**: Python code is executed line by line, which makes debugging easier.
- **Cross-platform**: It runs on multiple operating systems like Windows, macOS, and Linux.
- **Open Source**: Python is freely available and can be distributed and modified, benefiting from community contributions.
- **Extensive Libraries**: A vast standard library provides modules for numerous functionalities.
- **Object-Oriented**: Python supports OOP with classes and objects.
- **Integration**: It can be integrated with languages like C and C++.
- **Dynamic Typing**: Python does dynamic type checking.
- **Extensibility**: Programmers can add low-level modules to the Python interpreter.
- **Database Connectivity**: It supports interaction with most databases.
- **Automatic Memory Management**: Features garbage collection to manage memory usage.

## **First Python Program**

Python is known for its straightforward syntax that is similar to the English language. Here's how you can write and run your first Python program.

### Writing Your First Program

Create a new text file with the `.py` extension, for example, `hello.py`. Then, open it in a text editor and write your first program:

```python
# hello.py
print("Hello, Broadridge!")
```

This program uses the print() function to send the output to the screen.

### Running Your First Program

To run your Python program, open your command prompt or terminal, navigate to the directory containing your hello.py file, and then type:

```bash
python hello.py
```

If Python is installed correctly and the PATH is set, you should see the following output:

```bash
Hello, Broadridge!

```

!!! success
    **Congratulations!** You've just written and run your first Python program.


In Python, the basic syntax is simple and clean, which makes the code very easy to read and write. Here's an overview of the basic syntax, variables, and data types in Python:

## **Basic Syntax**

- **Comments**: Use the hash symbol (#) for single-line comments. For multi-line comments, you can use triple quotes (''' or """).
- **Indentation**: Python uses indentation to define blocks of code. The standard practice is to use 4 spaces per indentation level.
- **Case Sensitivity**: Python is case-sensitive. For example, Variable and variable are two different identifiers.
- **Statements**: Instructions that a Python interpreter can execute are called statements. For example, print("Hello, world!") is a statement.

For Example,

```py linenums="1"
# basic syntax.py

# Single Line Comment

"""
Line 1
Line 2
Line 3
Multi-Line Comment
"""


def hello():
    print("Hello, Broadridge")  # Observe Indentation


variable = 10
VARIABLE = "A"

if variable == VARIABLE:
    print("True")  # Observe Indentation
else:
    print("False")


print("Bingo!")  # Statements
print("Python is Awsome!")  # Statements
```
  
## **Variables**

- **Declaration**: Variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. E.g., x = 10.
- **Dynamic Typing**: Python is dynamically-typed, which means you can reassign variables to different data types. E.g., x = "Hello" is valid even after x = 10.
- **Immutable Variables**: Some of Python's internal data types, like strings and numbers, are immutable, meaning their contents cannot be changed after they are created.

For Example,

```python linenums="1"
# variables.py

x = 10
print(x)

x = "hello"
print(x)

```

## **Data Types**

### **Primitive Types**

- **Numbers**: Integers (int), floating-point numbers (float), and complex numbers (complex).
- **Strings**: Ordered sequences of characters, e.g., "Hello, world!".
- **Booleans**: Represents True or False values.

### **Data Structures**

- **Lists**: Ordered and mutable collections, e.g., [1, 2, 3].
- **Tuples**: Ordered and immutable collections, e.g., (1, 2, 3).
- **Dictionaries**: Unordered and mutable collections of key-value pairs, e.g., {"name": "Alice", "age": 25}.
- **Sets**: Unordered collections of unique elements, e.g., {1, 2, 3}.

!!! info
    To get the type of a Variable or a Data Structure in Python We can use **type(var)** Inbuilt Function

For Example,

```py linenums="1"
# Primitive types

a = 10
print(type(a))

b = 55.55
print(type(b))

c = 1 + 2j
print(c)
print(c.real)
print(c.imag)
print(type(c))

d = "hello"
print(type(d))

e = True
print(type(e))

# Data Structures

f = [1, 2, 3, 4, 5]
print(type(f))

g = (1, 2, 3, 4, 5)
print(type(g))

h = {"a": 1, "b": 2, "c": 3}
print(type(h))

i = {1, 2, 3, 4, 5}
print(type(i))

```

These are the fundamental elements you'll use when starting to code in Python. Remember, Python is designed to be easy to understand and fun to use, which is why its syntax is often considered one of its greatest strengths.

## **Operators in Python**

Python includes several types of operators:

### **Arithmetic Operators** 

Perform mathematical operations like addition (+), subtraction (-), multiplication (*), division (/), modulus (%), exponentiation (**), and floor division (//).

For Example,

```py linenums="1"
# Arithmetic Operators in Python

# Addition
addition = 5 + 3
print("Addition: 5 + 3 =", addition)

# Subtraction
subtraction = 5 - 3
print("Subtraction: 5 - 3 =", subtraction)

# Multiplication
multiplication = 5 * 3
print("Multiplication: 5 * 3 =", multiplication)

# Division
division = 5 / 3
print("Division: 5 / 3 =", division)

# Modulus (Remainder)
modulus = 5 % 3
print("Modulus: 5 % 3 =", modulus)

# Exponentiation (Power)
exponentiation = 5**3
print("Exponentiation: 5 ** 3 =", exponentiation)

# Floor Division
floor_division = 5 // 3
print("Floor Division: 5 // 3 =", floor_division)

```

### **Comparison Operators**

Compare values and include equals (==), not equals (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=).

For Example,

```py linenums="1"
# Comparison Operators in Python

# Equals: ==
equals = 5 == 3
print("Equals: 5 == 3 is", equals)

# Not Equals: !=
not_equals = 5 != 3
print("Not Equals: 5 != 3 is", not_equals)

# Greater than: >
greater_than = 5 > 3
print("Greater than: 5 > 3 is", greater_than)

# Less than: <
less_than = 5 < 3
print("Less than: 5 < 3 is", less_than)

# Greater than or equal to: >=
greater_than_or_equal_to = 5 >= 3
print("Greater than or equal to: 5 >= 3 is", greater_than_or_equal_to)

# Less than or equal to: <=
less_than_or_equal_to = 5 <= 3
print("Less than or equal to: 5 <= 3 is", less_than_or_equal_to)

```

### **Logical Operators**

Used for logical operations, primarily with boolean values, including and, or, and not.

For Example,

```py linenums="1"
# Logical Operators in Python

# Logical AND
logical_and = True and False
print("Logical AND (True and False) is", logical_and)

# Logical OR
logical_or = True or False
print("Logical OR (True or False) is", logical_or)

# Logical NOT
logical_not = not True
print("Logical NOT (not True) is", logical_not)

# Combining Logical Operators
combined_logical = (True and False) or (not False)
print("Combined Logical ((True and False) or (not False)) is", combined_logical)
```

### **Assignment Operators**

Assign values to variables, e.g., =, +=, -=, *=, /=, etc.

For Example,

```py linenums="1"
# Assignment Operators in Python

# Simple Assignment =
x = 10
print("Simple Assignment: x =", x)

# Add AND (+=)
x += 3  # Equivalent to x = x + 3
print("Add AND (+=): x =", x)

# Subtract AND (-=)
x -= 2  # Equivalent to x = x - 2
print("Subtract AND (-=): x =", x)

# Multiply AND (*=)
x *= 2  # Equivalent to x = x * 2
print("Multiply AND (*=): x =", x)

# Divide AND (/=)
x /= 4  # Equivalent to x = x / 4
print("Divide AND (/=): x =", x)

# Modulus AND (%=)
x %= 3  # Equivalent to x = x % 3
print("Modulus AND (%=): x =", x)

# Exponent AND (**=)
x **= 2  # Equivalent to x = x ** 2
print("Exponent AND (**=): x =", x)

# Floor Division AND (//=)
x //= 2  # Equivalent to x = x // 2
print("Floor Division AND (//=): x =", x)
```

### **Identity Operators**

`is` and `is not` check if two variables refer to the same object in memory.

For Example,

```py linenums="1"
# Identity Operators in Python

# 'is' and 'is not' operators

# is: Evaluates to True if the variables on either side of the operator point to the same object # Noqa
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("x is z:", x is z)
print("x is y:", x is y)
print("x == y:", x == y)

# is not: Evaluates to True if the variables on either side of the operator do not point to the same object # Noqa
print("x is not y:", x is not y)

```

### **Membership Operators**

`in` and `not in` check for membership in a sequence, such as lists or strings.

For Example,

```py linenums="1"
# Membership Operators in Python

# 'in' and 'not in' operators

# in: Evaluates to True if the specified value is found in the sequence
fruits = ["apple", "banana", "cherry"]
print("Is 'apple' in fruits?", "apple" in fruits)
print("Is 'orange' in fruits?", "orange" in fruits)

# not in: Evaluates to True if the specified value is not found in the sequence
print("Is 'mango' not in fruits?", "mango" not in fruits)
print("Is 'banana' not in fruits?", "banana" not in fruits)

```

### **Bitwise Operators**

Perform bitwise calculations on integers, including & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), and >> (right shift).

For Example,

```py linenums="1"
# Bitwise Operators in Python

# Bitwise AND (&)
a = 12  # 1100 in binary
b = 15  # 1111 in binary
print("Bitwise AND (a & b):", a & b)  # Result is 1100 in binary which is 12 in decimal

# Bitwise OR (|)
print("Bitwise OR (a | b):", a | b)  # Result is 1111 in binary which is 15 in decimal

# Bitwise XOR (^)
print("Bitwise XOR (a ^ b):", a ^ b)  # Result is 0011 in binary which is 3 in decimal

# Bitwise NOT (~)
print("Bitwise NOT (~a):", ~a)  # Result is -13, which is the two's complement of 12

# Bitwise Left Shift (<<)
print("Bitwise Left Shift (a << 2):", a << 2)  # Left shift the bits of a by 2, result is 48

# Bitwise Right Shift (>>)
print("Bitwise Right Shift (a >> 2):", a >> 2)  # Right shift the bits of a by 2, result is 3

```