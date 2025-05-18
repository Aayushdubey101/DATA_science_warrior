# Variables and Operators in Python

## Introduction to Variables
In Python, a variable is a name that refers to a value stored in the computer's memory. Variables allow you to store data and manipulate it throughout your program. Unlike some other programming languages, Python does not require you to declare the type of a variable explicitly; the type is inferred from the value assigned.

## Rules for Declaring Variables
When declaring variables in Python, you must follow these rules:

- Variable names must start with a letter (a-z, A-Z) or an underscore (_).
- The rest of the variable name can contain letters, digits (0-9), or underscores.
- Variable names are case-sensitive (`myVar` and `myvar` are different variables).
- Variable names cannot be Python reserved keywords (such as `if`, `for`, `while`, `class`, etc.).
- Variable names should not contain spaces or special characters (like `@`, `#`, `$`, etc.).

## Variable Naming Conventions
While the above rules define what is allowed, it is good practice to follow these conventions:

- Use lowercase letters with words separated by underscores for readability (e.g., `my_variable`).
- Use descriptive names that clearly indicate the purpose of the variable.
- Avoid using single-character names except for counters or iterators in loops.

## Data Types Overview
Python supports several built-in data types, including:

- **int**: Integer numbers, e.g., `5`, `-10`
- **float**: Floating-point numbers (decimals), e.g., `3.14`, `-0.001`
- **str**: Strings (text), e.g., `"Hello"`, `'Python'`
- **bool**: Boolean values, `True` or `False`
- **list**, **tuple**, **dict**, etc.: Collection data types (covered in later units)

## Assigning Values to Variables
You assign a value to a variable using the assignment operator `=`:

```python
a = 3  # a is a variable name and 3 is an integer data type
b = 2  # b is a variable name and 2 is an integer data type
pi = 3.14  # floating point number
is_valid = True  # boolean value
```

You can also reassign a variable to a new value at any time:

```python
a = 7
a = a + 3  # a is now 10
```

## Operators in Python
Operators are special symbols that perform operations on variables and values.

### Arithmetic Operators
- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division (returns float)
- `//`: Floor division (returns integer)
- `%` : Modulus (remainder)
- `**`: Exponentiation (power)

Example:

```python
x = 8
y = 5

print('Sum total: ', x + y)  # 13
print('Difference: ', x - y)  # 3
print('Product: ', x * y)  # 40
print('Division result: ', 10 / 2)  # 5.0
print('Division result: ', 15 / 3)  # 5.0
print('Division result: ', 9 / 4)  # 2.25
print('Floor division result: ', 9 // 4)  # 2
print('Remainder: ', 10 % 3)  # 1
print('Floor division result: ', 15 // 4)  # 3
print('Power: ', 2 ** 4)  # 16
```

### Comparison Operators
Used to compare two values, returning a Boolean result:

- `==` : Equal to
- `!=` : Not equal to
- `>`  : Greater than
- `<`  : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

Example:

```python
x = 5
y = 10

print(3 > 2)     # True
print(3 >= 2)    # True
print(3 < 2)     # False
print(2 < 3)     # True
print(2 <= 3)    # True
print(3 == 2)    # False
print(3 != 2)    # True
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False
```

### Logical Operators
Used to combine conditional statements:

- `and` : True if both operands are true
- `or`  : True if at least one operand is true
- `not` : Negates the Boolean value

Example:

```python
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

print('1 is 1', 1 is 1)                   # True
print('1 is not 2', 1 is not 2)           # True
print('A in Aayush', 'A' in 'Aayush') # True
print('B in Aayush', 'B' in 'Aayush') # False
print('coding' in 'coding for all') # True
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True
print(3 > 2 and 4 < 3) # False
print(3 < 2 and 4 < 3) # False
print(3 > 2 or 4 > 3)  # True
print(3 > 2 or 4 < 3)  # True
print(3 < 2 or 4 < 3)  # False
print(not 3 > 2)     # False
print(not True)      # False
print(not False)     # True
print(not not True)  # True
print(not not False) # False
```

## Summary
In this unit, you learned about variables, how to declare them following Python's rules, and the different types of operators you can use to manipulate data. Understanding these basics is essential for writing effective Python programs.
