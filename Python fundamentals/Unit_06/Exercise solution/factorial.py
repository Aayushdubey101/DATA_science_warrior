def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(10))
