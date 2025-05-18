import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)

print(solve_quadratic_eqn(1, -3, 2))  # x^2 - 3x + 2 = 0
print(solve_quadratic_eqn(1, -2, 1))  # x^2 - 2x + 1 = 0
print(solve_quadratic_eqn(1, 1, 1))   # x^2 + x + 1 = 0
