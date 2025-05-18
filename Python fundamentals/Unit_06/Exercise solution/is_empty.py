def is_empty(param):
    if param:
        return False
    return True

print(is_empty([]))
print(is_empty([1, 2, 3]))
print(is_empty(""))
print(is_empty("Hello"))
print(is_empty({}))
print(is_empty(0))
print(is_empty(None))
