# Advanced Functions in Python

In Python, functions are first-class citizens, which means they can be treated like any other object. This allows you to:

- Pass functions as arguments to other functions
- Return functions from other functions
- Assign functions to variables
- Modify functions dynamically

This section covers:

1. Functions as parameters
2. Functions as return values
3. Closures
4. Decorators
5. Built-in higher order functions: map, filter, reduce
6. Exercises with solutions

## Functions as Parameters

You can pass a function as an argument to another function. This is useful for creating flexible and reusable code.

```py
def multiply_by_two(x):
    return x * 2

def apply_function(func, value):
    return func(value)

result = apply_function(multiply_by_two, 5)
print(result)  # Output: 10
```

## Functions as Return Values

Functions can return other functions. This allows you to create function factories or customize behavior dynamically.

```py
def make_power_function(power):
    def power_function(x):
        return x ** power
    return power_function

square = make_power_function(2)
cube = make_power_function(3)

print(square(4))  # Output: 16
print(cube(2))    # Output: 8
```

## Closures

A closure is a nested function that remembers the values from its enclosing scope even if the outer function has finished executing.

```py
def greeting_maker(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

hello = greeting_maker("Hello")
hi = greeting_maker("Hi")

print(hello("Alice"))  # Output: Hello, Alice!
print(hi("Bob"))       # Output: Hi, Bob!
```

## Decorators

Decorators are functions that modify the behavior of other functions. They are often used to add functionality like logging, timing, or access control.

### Creating a Decorator

```py
def decorator(func):
    def wrapper():
        print("Before the function call")
        result = func()
        print("After the function call")
        return result
    return wrapper

def say_hello():
    print("Hello!")

decorated_say_hello = decorator(say_hello)
decorated_say_hello()
```

### Using the @ Syntax

```py
def decorator(func):
    def wrapper():
        print("Before the function call")
        result = func()
        print("After the function call")
        return result
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
```

### Multiple Decorators

```py
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclaim_decorator(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper

@exclaim_decorator
@uppercase_decorator
def greet():
    return "hello"

print(greet())  # Output: HELLO!
```

### Decorators with Parameters

```py
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```

## Built-in Higher Order Functions

### map()

The `map()` function applies a function to all items in an iterable.

```py
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

squared = map(square, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Using lambda
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]
```

### filter()

The `filter()` function filters items out of an iterable based on a function that returns True or False.

```py
numbers = [1, 2, 3, 4, 5]

def is_even(x):
    return x % 2 == 0

evens = filter(is_even, numbers)
print(list(evens))  # Output: [2, 4]

# Using lambda
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4]
```

### reduce()

The `reduce()` function applies a rolling computation to sequential pairs of values in an iterable. It is in the `functools` module.

```py
from functools import reduce

numbers = [1, 2, 3, 4, 5]

def add(x, y):
    return x + y

total = reduce(add, numbers)
print(total)  # Output: 15

# Using lambda
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15
```

## 💻 Exercises and Solutions

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Level 1

1. Explain the difference between map, filter, and reduce.

- `map` applies a function to each item in an iterable and returns a new iterable with the results.
- `filter` applies a function that returns True or False to each item and returns a new iterable with only the items where the function returned True.
- `reduce` applies a function cumulatively to the items of an iterable, reducing it to a single value.

2. Explain the difference between higher order function, closure and decorator.

- A higher order function is a function that takes another function as an argument or returns a function.
- A closure is a nested function that remembers the environment in which it was created.
- A decorator is a function that modifies another function, usually by wrapping it.

3. Define a call function before map, filter or reduce, see examples.

```py
def square(x):
    return x ** 2

print(list(map(square, numbers)))
print(list(filter(lambda x: x % 2 == 0, numbers)))

from functools import reduce
print(reduce(lambda x, y: x + y, numbers))
```

4. Use for loop to print each country in the countries list.

```py
for country in countries:
    print(country)
```

5. Use for to print each name in the names list.

```py
for name in names:
    print(name)
```

6. Use for to print each number in the numbers list.

```py
for number in numbers:
    print(number)
```

### Level 2

1. Use map to create a new list by changing each country to uppercase in the countries list.

```py
upper_countries = list(map(lambda c: c.upper(), countries))
print(upper_countries)
```

2. Use map to create a new list by changing each number to its square in the numbers list.

```py
squares = list(map(lambda x: x ** 2, numbers))
print(squares)
```

3. Use map to change each name to uppercase in the names list.

```py
upper_names = list(map(lambda n: n.upper(), names))
print(upper_names)
```

4. Use filter to filter out countries containing 'land'.

```py
land_countries = list(filter(lambda c: 'land' in c, countries))
print(land_countries)
```

5. Use filter to filter out countries having exactly six characters.

```py
six_char_countries = list(filter(lambda c: len(c) == 6, countries))
print(six_char_countries)
```

6. Use filter to filter out countries containing six letters and more in the country list.

```py
six_or_more_countries = list(filter(lambda c: len(c) >= 6, countries))
print(six_or_more_countries)
```

7. Use filter to filter out countries starting with an 'E'.

```py
e_countries = list(filter(lambda c: c.startswith('E'), countries))
print(e_countries)
```

8. Chain two or more list iterators (e.g., map, filter, reduce).

```py
from functools import reduce

result = reduce(lambda x, y: x + y,
                map(lambda x: x.upper(),
                    filter(lambda c: 'land' in c, countries)))
print(result)
```

9. Declare a function called get_string_lists which takes a list as a parameter and returns a list containing only string items.

```py
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

mixed_list = [1, 'hello', 3.14, 'world']
print(get_string_lists(mixed_list))  # ['hello', 'world']
```

10. Use reduce to sum all the numbers in the numbers list.

```py
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print(total)
```

11. Use reduce to concatenate all the countries and produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.

```py
from functools import reduce

sentence = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ', and ' + countries[-1] + ' are north European countries.'
print(sentence)
```

12. Declare a function called categorize_countries that returns a list of countries with some common pattern (e.g., 'land', 'ia', 'island', 'stan').

```py
def categorize_countries(countries, pattern):
    return list(filter(lambda c: pattern in c, countries))

print(categorize_countries(countries, 'land'))
```

13. Create a function returning a dictionary where keys are starting letters of countries and values are the number of country names starting with that letter.

```py
def count_countries_by_letter(countries):
    result = {}
    for country in countries:
        first_letter = country[0]
        result[first_letter] = result.get(first_letter, 0) + 1
    return result

print(count_countries_by_letter(countries))
```

14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries list.

```py
def get_first_ten_countries(countries):
    return countries[:10]

print(get_first_ten_countries(countries))
```

15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

```py
def get_last_ten_countries(countries):
    return countries[-10:]

print(get_last_ten_countries(countries))
```

### Level 3

1. Use the countries_data.py file and follow the tasks below:

- Sort countries by name, by capital, by population
- Sort out the ten most spoken languages by location.
- Sort out the ten most populated countries.

```py
# Assuming countries_data is a list of dictionaries with keys: 'name', 'capital', 'population', 'languages'

# Sort countries by name
sorted_by_name = sorted(countries_data, key=lambda c: c['name'])
print([c['name'] for c in sorted_by_name])

# Sort countries by capital
sorted_by_capital = sorted(countries_data, key=lambda c: c['capital'])
print([c['capital'] for c in sorted_by_capital])

# Sort countries by population
sorted_by_population = sorted(countries_data, key=lambda c: c['population'], reverse=True)
print([c['name'] for c in sorted_by_population[:10]])

# Sort out the ten most spoken languages by location
from collections import Counter

languages = []
for country in countries_data:
    languages.extend(country['languages'])

language_counts = Counter(languages)
most_spoken = language_counts.most_common(10)
print(most_spoken)
