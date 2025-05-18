import keyword
import re

def is_valid_variable(name):
    # Check if string is empty
    if not name:
        return False
    
    # Check if it's a keyword
    if keyword.iskeyword(name):
        return False
    
    # Match regex pattern for valid identifier
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, name))

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))
print(is_valid_variable('for'))
print(is_valid_variable('_name'))
