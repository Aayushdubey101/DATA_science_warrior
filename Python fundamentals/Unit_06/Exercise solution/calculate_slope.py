def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return float('inf')  # Vertical line has infinite slope
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(1, 2, 3, 6))
print(calculate_slope(0, 0, 5, 5))
print(calculate_slope(1, 1, 1, 5))  # Vertical line
