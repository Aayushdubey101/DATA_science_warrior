# Tuples

A tuple is a group of items that are ordered and cannot be changed (immutable). Tuples use round brackets () to hold the items. Once you make a tuple, you cannot change its items. Unlike lists, tuples have fewer methods because they cannot be changed.

## How to Make a Tuple

- Empty tuple:

```python
empty = ()
# or
empty = tuple()
```

- Tuple with items:

```python
colors = ('red', 'blue', 'green')
```

## How to Find the Length of a Tuple

Use the `len()` function to find out how many items are in a tuple.

```python
colors = ('red', 'blue', 'green')
print(len(colors))  # Output: 3
```

## How to Get Items from a Tuple

You can get items by their position using indexing. Indexing starts at 0.

- Positive indexing:

```python
colors = ('red', 'blue', 'green')
first = colors[0]   # 'red'
second = colors[1]  # 'blue'
```

- Negative indexing (from the end):

```python
colors = ('red', 'blue', 'green')
last = colors[-1]   # 'green'
second_last = colors[-2]  # 'blue'
```

## How to Get a Part of a Tuple (Slicing)

You can get a part of a tuple by slicing it.

```python
colors = ('red', 'blue', 'green', 'yellow')
first_two = colors[0:2]  # ('red', 'blue')
last_two = colors[-2:]   # ('green', 'yellow')
```

## Changing a Tuple

Tuples cannot be changed directly. But you can convert a tuple to a list, change the list, then convert it back.

```python
colors = ('red', 'blue', 'green')
colors_list = list(colors)
colors_list[0] = 'purple'
colors = tuple(colors_list)
print(colors)  # ('purple', 'blue', 'green')
```

## Check if an Item is in a Tuple

Use the `in` keyword to check if an item is in a tuple.

```python
colors = ('red', 'blue', 'green')
print('blue' in colors)  # True
print('yellow' in colors)  # False
```

## Joining Tuples

You can join two tuples using the `+` operator.

```python
a = ('red', 'blue')
b = ('green', 'yellow')
c = a + b
print(c)  # ('red', 'blue', 'green', 'yellow')
```

## Deleting a Tuple

You cannot delete items in a tuple, but you can delete the whole tuple.

```python
colors = ('red', 'blue', 'green')
del colors
```

---

You have learned the basics of tuples with simple examples. Keep practicing to get better!
