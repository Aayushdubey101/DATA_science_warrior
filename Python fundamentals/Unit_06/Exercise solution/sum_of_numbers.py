def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))
