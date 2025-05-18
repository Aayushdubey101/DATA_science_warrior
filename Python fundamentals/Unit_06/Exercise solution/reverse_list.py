def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))
