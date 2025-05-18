Exception Handling in Python

In Python, errors can be managed using the _try_ and _except_ statements, allowing programs to handle unexpected situations without crashing. This approach, known as graceful error handling, ensures that when an error occurs, the program responds in a controlled way, often by displaying a helpful message. Errors can arise from various external factors such as invalid user input, missing files, or hardware issues. Proper handling of these exceptions makes your programs more reliable and user-friendly.

Previously, we explored different types of errors in Python. By using _try_ and _except_, you can prevent your program from stopping abruptly when an error occurs within the _try_ block.



```py
try:
    # Code that might cause an error
except:
    # Code that runs if an error occurs
```

**Example:**

```py
try:
    result = 5 + '3'
except:
    print('An error occurred during addition.')
```

In this example, adding a number and a string causes an error. Instead of crashing, the program prints a message from the _except_ block.

**Example:**

```py
try:
    username = input('Please enter your username: ')
    birth_year = input('Please enter your birth year: ')
    age = 2024 - birth_year
    print(f'Hello {username}, you are {age} years old.')
except:
    print('Oops! Something went wrong.')
```

```sh
Oops! Something went wrong.
```

Here, the program fails silently without specifying the error. To get more detailed information, you can catch specific error types.

The following example handles different error types and informs you about the exact issue:

```py
try:
    username = input('Please enter your username: ')
    birth_year = input('Please enter your birth year: ')
    age = 2024 - birth_year
    print(f'Hello {username}, you are {age} years old.')
except TypeError:
    print('A TypeError has occurred.')
except ValueError:
    print('A ValueError has occurred.')
except ZeroDivisionError:
    print('A ZeroDivisionError has occurred.')
```

```sh
Please enter your username: Alice
Please enter your birth year: 1990
A TypeError has occurred.
```

In this case, the error is a _TypeError_ because the subtraction operation involves incompatible types.

Let's improve the code by converting the input to an integer and adding _else_ and _finally_ blocks:

```py
try:
    username = input('Please enter your username: ')
    birth_year = input('Please enter your birth year: ')
    age = 2024 - int(birth_year)
    print(f'Hello {username}, you are {age} years old.')
except TypeError:
    print('A TypeError has occurred.')
except ValueError:
    print('A ValueError has occurred.')
except ZeroDivisionError:
    print('A ZeroDivisionError has occurred.')
else:
    print('The try block executed successfully.')
finally:
    print('This block always runs.')
```

```sh
Please enter your username: Alice
Please enter your birth year: 1990
Hello Alice, you are 34 years old.
The try block executed successfully.
This block always runs.
```

You can also simplify error handling by catching all exceptions using the base _Exception_ class:

```py
try:
    username = input('Please enter your username: ')
    birth_year = input('Please enter your birth year: ')
    age = 2024 - int(birth_year)
    print(f'Hello {username}, you are {age} years old.')
except Exception as error:
    print(f'Error: {error}')
