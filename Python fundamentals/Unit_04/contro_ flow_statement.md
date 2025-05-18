# Control Flow Statements in Python

## Introduction
Control flow statements allow you to control the execution flow of your program based on conditions or repeated execution of code blocks. They are essential for making decisions and performing repetitive tasks.

## Conditional Statements: if, elif, else
The `if` statement executes a block of code if a specified condition is true. You can use `elif` (else if) to check multiple conditions, and `else` to execute code if none of the conditions are met.

### Syntax:
```python
if condition1:
    # code block 1
elif condition2:
    # code block 2
else:
    # code block 3
```

### Example:
```python
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
```

## For Loops
The `for` loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item.

### Syntax:
```python
for item in sequence:
    # code block
```

### Example:
```python
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)
```

## While Loops
The `while` loop repeatedly executes a block of code as long as a specified condition is true.

### Syntax:
```python
while condition:
    # code block
```

### Example:
```python
count = 0

while count < 5:
    print(count)
    count += 1
```

## Summary
Control flow statements like `if`, `elif`, `else`, `for`, and `while` loops are fundamental to writing dynamic and flexible Python programs. They allow you to make decisions and repeat actions efficiently.
