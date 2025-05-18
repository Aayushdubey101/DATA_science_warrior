# 10 Simple DSA Loop Examples without imports or functions

# 1. Print first N natural numbers
n = 10
print("1. First N natural numbers:")
for i in range(1, n+1):
    print(i, end=' ')
print("\n")

# 2. Print first N even numbers
print("2. First N even numbers:")
for i in range(1, n+1):
    print(2*i, end=' ')
print("\n")

# 3. Sum of first N natural numbers
total = 0
for i in range(1, n+1):
    total += i
print("3. Sum of first N natural numbers:", total)
print("\n")

# 4. Factorial of a number
num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print("4. Factorial of", num, "is", fact)
print("\n")

# 5. Reverse a number
number = 12345
rev = 0
temp = number
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("5. Reverse of", number, "is", rev)
print("\n")

# 6. Check if a number is prime
prime_candidate = 29
is_prime = True
if prime_candidate < 2:
    is_prime = False
else:
    for i in range(2, prime_candidate):
        if prime_candidate % i == 0:
            is_prime = False
            break
print("6.", prime_candidate, "is prime:", is_prime)
print("\n")

# 7. Print Fibonacci series up to N terms
print("7. Fibonacci series up to", n, "terms:")
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print("\n")

# 8. Find the largest element in a list
lst = [3, 5, 7, 2, 8, 1, 4]
max_val = lst[0]
for val in lst:
    if val > max_val:
        max_val = val
print("8. Largest element in list:", max_val)
print("\n")

# 9. Count digits in a number
num_to_count = 1234567890
count = 0
temp = num_to_count
while temp > 0:
    temp //= 10
    count += 1
print("9. Number of digits in", num_to_count, "is", count)
print("\n")

# 10. Check if a number is palindrome
pal_num = 12321
temp = pal_num
rev_num = 0
while temp > 0:
    rev_num = rev_num * 10 + temp % 10
    temp //= 10
print("10.", pal_num, "is palindrome:", pal_num == rev_num)
