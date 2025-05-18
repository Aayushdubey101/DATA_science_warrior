def is_unique_list(lst):
    return len(lst) == len(set(lst))

print(is_unique_list([1, 2, 3, 4, 5]))
print(is_unique_list([1, 2, 3, 3, 5]))
print(is_unique_list(['a', 'b', 'c']))
print(is_unique_list(['a', 'b', 'c', 'b']))
