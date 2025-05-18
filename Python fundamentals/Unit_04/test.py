# Solutions to 3 questions using conditional flow statements

# Question 1: Check if a number is positive, negative, or zero
number = 10

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Question 2: Determine if a person is eligible to vote based on age
age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# Question 3: Find the largest of three numbers
a = 5
b = 10
c = 7

if a >= b and a >= c:
    print(f"{a} is the largest number.")
elif b >= a and b >= c:
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number.")

# Question 4: Categorize a data value based on thresholds (Data Science example)
value = 75

if value >= 90:
    print("Grade: A")
elif value >= 75:
    print("Grade: B")
elif value >= 60:
    print("Grade: C")
else:
    print("Grade: F")
