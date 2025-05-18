## Sets

A set is a collection of unique elements. Think back to your basic math classes where sets were introduced. In Python, a set is an unordered collection of distinct items without any indexing. Sets are useful for storing unique values and support operations like _union_, _intersection_, _difference_, _symmetric difference_, _subset_, _superset_, and _disjoint_ checks.

### How to Create a Set

You can create a set using the built-in _set()_ function.

- Creating an empty set:

```py
# syntax
my_set = set()
```

- Creating a set with initial elements:

```py
# syntax
my_set = {'element1', 'element2', 'element3'}
```

**Example:**

```py
colors = {'red', 'blue', 'green', 'yellow'}
```

### Finding the Size of a Set

Use the **len()** function to get the number of elements in a set.

```py
# syntax
my_set = {'element1', 'element2', 'element3'}
len(my_set)
```

**Example:**

```py
colors = {'red', 'blue', 'green', 'yellow'}
len(colors)
```

### Accessing Elements in a Set

Since sets are unordered, you cannot access elements by index. Instead, use loops to iterate over the items. This will be covered in the loops section.

### Checking for an Element

To check if an element exists in a set, use the _in_ keyword.

```py
# syntax
my_set = {'element1', 'element2', 'element3'}
print('element2' in my_set)  # True
```

**Example:**

```py
colors = {'red', 'blue', 'green', 'yellow'}
print('blue' in colors)  # True
```

### Adding Elements to a Set

Sets are mutable, so you can add new elements after creation.

- Add a single element with _add()_:

```py
# syntax
my_set = {'element1', 'element2'}
my_set.add('element3')
```

**Example:**

```py
colors = {'red', 'blue', 'green'}
colors.add('purple')
```

- Add multiple elements with _update()_:

The _update()_ method accepts an iterable like a list or tuple.

```py
# syntax
my_set = {'element1', 'element2'}
my_set.update(['element3', 'element4'])
```

**Example:**

```py
colors = {'red', 'blue', 'green'}
new_colors = ('orange', 'pink', 'black')
colors.update(new_colors)
```

### Removing Elements from a Set

You can remove elements using _remove()_ or _discard()_. The difference is that _remove()_ raises an error if the element is not found, while _discard()_ does not.

```py
# syntax
my_set = {'element1', 'element2', 'element3'}
my_set.remove('element2')
```

The _pop()_ method removes and returns an arbitrary element from the set.

**Example:**

```py
colors = {'red', 'blue', 'green'}
removed_color = colors.pop()
```

### Clearing a Set

To empty a set, use the _clear()_ method.

```py
# syntax
my_set = {'element1', 'element2'}
my_set.clear()
```

**Example:**

```py
colors = {'red', 'blue', 'green'}
colors.clear()
print(colors)  # set()
```

### Deleting a Set

To delete a set entirely, use the _del_ statement.

```py
# syntax
my_set = {'element1', 'element2'}
del my_set
```

**Example:**

```py
colors = {'red', 'blue', 'green'}
del colors
```

### Converting Between Lists and Sets

You can convert a list to a set to remove duplicates, and convert a set back to a list.

```py
# syntax
my_list = ['a', 'b', 'a', 'c']
my_set = set(my_list)  # {'a', 'b', 'c'}
```

**Example:**

```py
fruits = ['apple', 'banana', 'apple', 'orange']
unique_fruits = set(fruits)  # {'apple', 'banana', 'orange'}
```

### Combining Sets

You can combine sets using _union()_ or _update()_.

- _union()_ returns a new set:

```py
# syntax
set1 = {'a', 'b'}
set2 = {'c', 'd'}
set3 = set1.union(set2)
```

**Example:**

```py
colors = {'red', 'blue'}
shapes = {'circle', 'square'}
combined = colors.union(shapes)
```

- _update()_ adds elements from one set into another:

```py
# syntax
set1 = {'a', 'b'}
set2 = {'c', 'd'}
set1.update(set2)
```

**Example:**

```py
colors = {'red', 'blue'}
shapes = {'circle', 'square'}
colors.update(shapes)
```

### Finding Common Elements (Intersection)

The _intersection()_ method returns elements common to both sets.

```py
# syntax
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c'}
set1.intersection(set2)  # {'b', 'c'}
```

**Example:**

```py
numbers = {1, 2, 3, 4, 5}
evens = {2, 4, 6, 8}
numbers.intersection(evens)  # {2, 4}
```

### Subset and Superset Checks

- _issubset()_ checks if a set is contained within another.
- _issuperset()_ checks if a set contains another.

```py
# syntax
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c'}
set2.issubset(set1)  # True
set1.issuperset(set2)  # True
```

**Example:**

```py
small_set = {1, 2}
large_set = {1, 2, 3, 4}
small_set.issubset(large_set)  # True
large_set.issuperset(small_set)  # True
```

### Finding Differences Between Sets

The _difference()_ method returns elements in one set but not the other.

```py
# syntax
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c'}
set1.difference(set2)  # {'a'}
```

**Example:**

```py
all_numbers = {1, 2, 3, 4, 5}
odd_numbers = {1, 3, 5}
all_numbers.difference(odd_numbers)  # {2, 4}
```

### Symmetric Difference Between Sets

The _symmetric_difference()_ method returns elements in either set but not in both.

```py
# syntax
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}
set1.symmetric_difference(set2)  # {'a', 'd'}
```

**Example:**

```py
setA = {1, 2, 3}
setB = {3, 4, 5}
setA.symmetric_difference(setB)  # {1, 2, 4, 5}
```

### Checking for Disjoint Sets

Two sets are disjoint if they have no elements in common. Use _isdisjoint()_ to check.

```py
# syntax
set1 = {'a', 'b'}
set2 = {'c', 'd'}
set1.isdisjoint(set2)  # True
```

**Example:**

```py
evens = {2, 4, 6}
odds = {1, 3, 5}
evens.isdisjoint(odds)  # True
```

🌟 Congratulations! You have completed the set operations overview. Now, try the exercises below to practice.

## 💻 Exercises: Sets Practice

```py
# Sample sets
tech_companies = {'Google', 'Apple', 'Microsoft', 'Amazon', 'Facebook'}
X = {10, 20, 30, 40, 50}
Y = {30, 40, 50, 60, 70}
ages = [20, 30, 40, 50, 30, 40]
```


