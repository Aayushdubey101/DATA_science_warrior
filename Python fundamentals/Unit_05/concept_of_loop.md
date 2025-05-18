# Concept of Loops in Python

## Introduction
Loops are fundamental programming constructs that allow you to execute a block of code repeatedly. They are essential for automating repetitive tasks and iterating over data structures such as lists, tuples, and dictionaries.

Python provides two primary types of loops:
- `for` loops
- `while` loops

## For Loops
A `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence.

### Syntax:
```python
for variable in sequence:
    # code block to execute
```

### Example:
```python
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
cherry
```

### Using `range()` with for loops
The `range()` function generates a sequence of numbers, which is commonly used with for loops.

Example:
```python
for i in range(5):
    print(i)
```
Output:
```
0
1
2
3
4
```

## While Loops
A `while` loop repeatedly executes a block of code as long as a specified condition is true.

### Syntax:
```python
while condition:
    # code block to execute
```

### Example:
```python
count = 0

while count < 5:
    print(count)
    count += 1
```
Output:
```
0
1
2
3
4
```

## Loop Control Statements
Python provides control statements to modify the behavior of loops:

- `break`: Terminates the loop prematurely.
- `continue`: Skips the current iteration and moves to the next.
- `else`: Executes a block of code once when the loop finishes normally (without encountering a `break`).

### Examples:

#### Using `break`
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```
Output:
```
0
1
2
3
4
```

#### Using `continue`
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```
Output:
```
0
1
3
4
```

#### Using `else` with loops
```python
for i in range(3):
    print(i)
else:
    print("Loop completed without break")
```
Output:
```
0
1
2
Loop completed without break
```

## Nested Loops
Loops can be nested inside other loops to perform more complex iterations.

Example:
```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```
Output:
```
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
```

## Summary
Loops are powerful tools in Python that help you automate repetitive tasks and process data efficiently. Understanding how to use `for` and `while` loops, along with control statements like `break` and `continue`, is essential for effective programming.
