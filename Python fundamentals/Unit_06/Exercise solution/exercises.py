# Solutions for exercises 1 and 2 from user_defined_function.md

def add_two_numbers(num1, num2):
    """
    Takes two parameters and returns their sum.
    """
    return num1 + num2

def area_of_circle(r):
    """
    Calculates the area of a circle given the radius r.
    area = π * r * r
    """
    PI = 3.141592653589793
    return PI * r * r

# Test the functions
if __name__ == "__main__":
    print("add_two_numbers(10, 20) =", add_two_numbers(10, 20))  # Expected: 30
    print("area_of_circle(5) =", area_of_circle(5))  # Expected: 78.53981633974483
