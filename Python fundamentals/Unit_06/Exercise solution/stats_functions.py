import statistics
import math

def calculate_mean(data):
    if not data:
        return None
    return sum(data) / len(data)

def calculate_median(data):
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]

def calculate_mode(data):
    if not data:
        return None
    
    frequency = {}
    for num in data:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    max_freq = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == max_freq]
    
    if len(modes) == len(data):
        return "No mode found"
    return modes

def calculate_range(data):
    if not data:
        return None
    return max(data) - min(data)

def calculate_variance(data):
    if not data or len(data) <= 1:
        return None
    
    mean = calculate_mean(data)
    squared_diff_sum = sum((x - mean) ** 2 for x in data)
    return squared_diff_sum / len(data)

def calculate_std(data):
    if not data or len(data) <= 1:
        return None
    
    variance = calculate_variance(data)
    return math.sqrt(variance)

data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
print(f"Mean: {calculate_mean(data)}")
print(f"Median: {calculate_median(data)}")
print(f"Mode: {calculate_mode(data)}")
print(f"Range: {calculate_range(data)}")
print(f"Variance: {calculate_variance(data)}")
print(f"Standard Deviation: {calculate_std(data)}")
