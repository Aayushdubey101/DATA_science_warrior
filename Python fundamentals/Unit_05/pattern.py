# Number of rows for the patterns
n = 5

# 1. Right Angled Triangle
print("Right Angled Triangle:")
for i in range(1, n+1):
    print('*' * i)

print("\nInverted Right Angled Triangle:")
# 2. Inverted Right Angled Triangle
for i in range(n, 0, -1):
    print('*' * i)

print("\nPyramid:")
# 3. Pyramid
for i in range(1, n+1):
    print(' ' * (n - i) + '* ' * i)

print("\nInverted Pyramid:")
# 4. Inverted Pyramid
for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)

print("\nDiamond:")
# 5. Diamond
for i in range(1, n+1):
    print(' ' * (n - i) + '* ' * i)
for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '* ' * i)

print("\nSquare Pattern:")
# 6. Square Pattern
for i in range(n):
    print('* ' * n)

print("\nHollow Square:")
# 7. Hollow Square
for i in range(n):
    if i == 0 or i == n-1:
        print('* ' * n)
    else:
        print('* ' + '  ' * (n-2) + '*')

print("\nRight Angled Triangle with Numbers:")
# 8. Right Angled Triangle with Numbers
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

print("\nFloyd's Triangle:")
# 9. Floyd's Triangle
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()

print("\nPascal's Triangle:")
# 10. Pascal's Triangle
for i in range(n):
    print(' ' * (n - i), end='')
    val = 1
    for j in range(i + 1):
        print(val, end=' ')
        val = val * (i - j) // (j + 1)
    print()
