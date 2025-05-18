def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "Error: All arguments must be numbers."
        total += num
    return total

print(add_all_nums(1, 2, 3, 4, 5))
print(add_all_nums(10, 20, 30))
print(add_all_nums(1, 2, "3"))
