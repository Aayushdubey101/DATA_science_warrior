def evens_and_odds(n):
    if n <= 0:
        return "Please provide a positive integer"
    
    evens = 0
    odds = 0
    
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

print(evens_and_odds(100))
