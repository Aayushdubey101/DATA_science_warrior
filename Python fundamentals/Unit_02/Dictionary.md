## Dictionaries

A dictionary is a collection of unordered, mutable paired (key: value) data type in Python.

### Creating a Dictionary

Dictionaries can be created using curly braces {} or the built-in *dict()* function.

```py
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'title':'The Great Gatsby', 'author':'F. Scott Fitzgerald', 'year':1925, 'genre':'Novel'}
```

**Example:**

```py
book = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'published_year': 1960,
    'genres': ['Southern Gothic', 'Bildungsroman'],
    'available': True,
    'ratings': {
        'goodreads': 4.28,
        'amazon': 4.8
    }
}
```

The dictionary above shows that values can be of any data type: string, boolean, list, dictionary, etc.

### Dictionary Length

The length of a dictionary is the number of key-value pairs it contains.

```py
# syntax
dct = {'title':'The Great Gatsby', 'author':'F. Scott Fitzgerald', 'year':1925, 'genre':'Novel'}
print(len(dct))  # 4
```

**Example:**

```py
print(len(book))  # 6
```

### Accessing Dictionary Items

Access dictionary items by referring to their key names.

```py
# syntax
dct = {'title':'The Great Gatsby', 'author':'F. Scott Fitzgerald'}
print(dct['title'])  # The Great Gatsby
```

**Example:**

```py
print(book['title'])           # To Kill a Mockingbird
print(book['genres'])          # ['Southern Gothic', 'Bildungsroman']
print(book['genres'][0])       # Southern Gothic
print(book['ratings']['goodreads'])  # 4.28
```

Accessing a key that does not exist raises a KeyError. To avoid this, use the *get()* method which returns None if the key is missing.

```py
print(book.get('publisher'))  # None
```

### Adding Items to a Dictionary

Add new key-value pairs by assigning a value to a new key.

```py
# syntax
dct = {'title':'The Great Gatsby'}
dct['pages'] = 218
```

**Example:**

```py
book['pages'] = 281
book['genres'].append('Classic')
print(book)
```

### Modifying Items in a Dictionary

Modify existing items by assigning a new value to an existing key.

```py
# syntax
dct = {'title':'The Great Gatsby'}
dct['title'] = 'The Great Gatsby (Revised Edition)'
```

**Example:**

```py
book['available'] = False
book['published_year'] = 1961
```

### Checking Keys in a Dictionary

Use the *in* operator to check if a key exists.

```py
# syntax
dct = {'title':'The Great Gatsby'}
print('title' in dct)  # True
print('publisher' in dct)  # False
```

### Removing Key and Value Pairs from a Dictionary

- *pop(key)*: removes the item with the specified key.
- *popitem()*: removes the last inserted item.
- *del*: deletes an item by key.

```py
# syntax
dct = {'title':'The Great Gatsby', 'author':'F. Scott Fitzgerald'}
dct.pop('author')  # removes 'author'
dct.popitem()      # removes last item
del dct['title']   # deletes 'title'
```

**Example:**

```py
book.pop('published_year')  # Removes 'published_year'
book.popitem()              # Removes last item (ratings)
del book['available']       # Deletes 'available'
```

### Changing Dictionary to a List of Items

The *items()* method returns a list of tuples representing the dictionary’s key-value pairs.

```py
# syntax
dct = {'title':'The Great Gatsby', 'author':'F. Scott Fitzgerald'}
print(dct.items())  # dict_items([('title', 'The Great Gatsby'), ('author', 'F. Scott Fitzgerald')])
```

### Clearing a Dictionary

Remove all items using the *clear()* method.

```py
# syntax
dct = {'title':'The Great Gatsby'}
dct.clear()
print(dct)  # {}
```

### Deleting a Dictionary

Delete the entire dictionary using *del*.

```py
# syntax
dct = {'title':'The Great Gatsby'}
del dct
```

### Copy a Dictionary

Create a copy to avoid mutating the original dictionary.

```py
# syntax
dct = {'title':'The Great Gatsby'}
dct_copy = dct.copy()
```

### Getting Dictionary Keys as a List

The *keys()* method returns all keys as a list-like object.

```py
# syntax
dct = {'title':'The Great Gatsby', 'author':'F. Scott Fitzgerald'}
keys = dct.keys()
print(keys)  # dict_keys(['title', 'author'])
```

### Getting Dictionary Values as a List

The *values()* method returns all values as a list-like object.

```py
# syntax
dct = {'title':'The Great Gatsby', 'author':'F. Scott Fitzgerald'}
values = dct.values()
print(values)  # dict_values(['The Great Gatsby', 'F. Scott Fitzgerald'])
```

🌟 Congratulations! You have now mastered dictionaries in Python. Practice using them with different examples to strengthen your understanding.
