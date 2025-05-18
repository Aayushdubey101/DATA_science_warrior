# Python Lists

Python has four main collection types:

- **List**: An ordered collection that can be changed. It allows duplicate items.
- **Tuple**: An ordered collection that cannot be changed. It allows duplicate items.
- **Set**: An unordered collection with no duplicates. You can add new items.
- **Dictionary**: An unordered collection of key-value pairs. It can be changed and does not allow duplicate keys.

## What is a List?

A list is an ordered collection of items. The items can be of different types. You can add, remove, or change items in a list. A list can also be empty.

## Creating a List

You can create a list in two ways:

- Using the `list()` function:

```python
empty_list = list()
print(len(empty_list))  # Output: 0
```

- Using square brackets `[]`:

```python
empty_list = []
print(len(empty_list))  # Output: 0
```

You can also create a list with initial items:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print(len(fruits))  # Output: 4
```

Lists can contain items of different types:

```python
mixed_list = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]
```

## Accessing List Items

List items have positions called indexes, starting at 0.

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[0])  # banana
print(fruits[1])  # orange
print(fruits[-1]) # lemon (last item)
```

## Unpacking Lists

You can assign list items to variables:

```python
lst = ['item1', 'item2', 'item3', 'item4']
first, second, *rest = lst
print(first)   # item1
print(second)  # item2
print(rest)    # ['item3', 'item4']
```

## Slicing Lists

Get parts of a list by specifying start and end positions:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[1:3])  # ['orange', 'mango']
print(fruits[:2])   # ['banana', 'orange']
print(fruits[::2])  # ['banana', 'mango']
print(fruits[::-1]) # ['lemon', 'mango', 'orange', 'banana'] (reversed)
```

## Changing List Items

Lists can be changed by assigning new values to positions:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)  # ['avocado', 'orange', 'mango', 'lemon']
```

## Checking if an Item Exists

Use `in` to check if an item is in a list:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print('banana' in fruits)  # True
print('lime' in fruits)    # False
```

## Adding Items

Add items to the end of a list with `append()`:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
```

Insert items at a specific position with `insert()`:

```python
fruits.insert(2, 'apple')
print(fruits)  # ['banana', 'orange', 'apple', 'mango', 'lemon']
```

## Removing Items

Remove an item by value with `remove()`:

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
```

Remove an item by position with `pop()`:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)  # ['banana', 'orange', 'mango']
fruits.pop(0)
print(fruits)  # ['orange', 'mango']
```

Remove items by position or range with `del`:

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1:3]
print(fruits)  # ['orange', 'lime']
```

Clear all items with `clear()`:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)  # []
```

## Copying Lists

Create a copy of a list with `copy()`:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon']
```

## Joining Lists

Join lists with `+` operator:

```python
list1 = [1, 2, 3]
list2 = [4, 5]
joined = list1 + list2
print(joined)  # [1, 2, 3, 4, 5]
```

Or use `extend()` to add items from one list to another:

```python
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5]
```

## Counting Items

Count how many times an item appears with `count()`:

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange']
print(fruits.count('orange'))  # 2
```

## Finding Index

Find the position of an item with `index()`:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))  # 1
```

## Reversing a List

Reverse the order of items with `reverse()`:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  # ['lemon', 'mango', 'orange', 'banana']
```

## Sorting Lists

Sort items with `sort()` (changes the list) or `sorted()` (returns a new list):

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)  # ['banana', 'lemon', 'mango', 'orange']

fruits = ['banana', 'orange', 'mango', 'lemon']
sorted_fruits = sorted(fruits, reverse=True)
print(sorted_fruits)  # ['orange', 'mango', 'lemon', 'banana']
```
<br >
<H1><u> Some Advanced concept</u><H1>

## List and Other Data Type Comprehensions

Comprehensions provide a concise way to create lists, sets, or dictionaries.

### List Comprehension

Create a new list by applying an expression to each item in an existing list:

```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]
```

### Set Comprehension

Create a set using comprehension syntax:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16, 25}
```

### Dictionary Comprehension

Create a dictionary from a list:

```python
numbers = [1, 2, 3, 4, 5]
square_dict = {x: x**2 for x in numbers}
print(square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Enumerate Function

The `enumerate()` function adds a counter to an iterable and returns it as an enumerate object.

```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry
```

You can also specify a starting index:

```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# Output:
# 1 apple
# 2 banana
# 3 cherry
```

## Packing and Unpacking

Packing allows you to assign multiple values to a single variable as a tuple, and unpacking allows you to extract values from a collection into variables.

### Packing

```python
packed = 1, 2, 3
print(packed)  # (1, 2, 3)
```

### Unpacking

```python
a, b, c = packed
print(a)  # 1
print(b)  # 2
print(c)  # 3
```

You can also use `*` to unpack multiple values:

```python
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```

## Zip Function

The `zip()` function combines multiple iterables (like lists or tuples) into tuples.

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(combined)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

You can unzip using the `*` operator:

```python
names, ages = zip(*combined)
print(names)  # ('Alice', 'Bob', 'Charlie')
print(ages)   # (25, 30, 35)
