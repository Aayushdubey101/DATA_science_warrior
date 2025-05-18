def is_same_data_type(lst):
    if not lst:
        return True
    
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    
    return True

print(is_same_data_type([1, 2, 3, 4]))
print(is_same_data_type(['a', 'b', 'c']))
print(is_same_data_type([1, 'a', 3]))
print(is_same_data_type([[], {}]))
