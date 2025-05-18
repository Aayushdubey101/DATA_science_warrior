# File Handling in Python

In programming, we often need to save data to files or read data from files. File handling allows us to create, read, update, and delete files using Python.

## Opening a File

To work with files, we use the built-in function `open()`. It takes the filename and mode as arguments.

```python
# Syntax
open('filename', 'mode')
```

Common modes are:
- `'r'` - Read (default). Opens a file for reading. Error if file does not exist.
- `'w'` - Write. Opens a file for writing. Creates file if it does not exist. Overwrites existing content.
- `'a'` - Append. Opens a file to add content at the end. Creates file if it does not exist.
- `'x'` - Create. Creates a new file. Error if file exists.
- `'t'` - Text mode (default).
- `'b'` - Binary mode (for images, etc.).

## Reading from a File

Example of reading a file named `example.txt`:

```python
f = open('example.txt', 'r')
content = f.read()
print(content)
f.close()
```

You can also read line by line:

```python
f = open('example.txt')
line = f.readline()
print(line)
f.close()
```

Or read all lines into a list:

```python
f = open('example.txt')
lines = f.readlines()
print(lines)
f.close()
```

## Writing to a File

To write to a file, open it in write (`'w'`) or append (`'a'`) mode:

```python
with open('example.txt', 'w') as f:
    f.write('This is a new line.\n')
```

Appending text:

```python
with open('example.txt', 'a') as f:
    f.write('This line is added at the end.\n')
```

Using `with` automatically closes the file after the block.

## Deleting a File

To delete a file, use the `os` module:

```python
import os

if os.path.exists('example.txt'):
    os.remove('example.txt')
    print('File deleted.')
else:
    print('File does not exist.')
```

## Common File Formats

- **Text files (.txt):** Simple text data.
- **JSON files (.json):** Store data in key-value pairs.
- **CSV files (.csv):** Store tabular data separated by commas.
- **Binary files (.bin):** Store binary data like images.

## Working with JSON Files

Example of reading JSON data:

```python
import json

with open('data.json', 'r') as f:
    data = json.load(f)
print(data)
```

Writing JSON data:

```python
import json

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
```

This is a simple overview of file handling in Python.
