def most_populated_countries(countries_data, n=10):
    sorted_countries = sorted(countries_data, key=lambda x: x.get('population', 0), reverse=True)
    
    result = []
    for i in range(min(n, len(sorted_countries))):
        country = sorted_countries[i]
        result.append({
            'name': country.get('name', ''),
            'population': country.get('population', 0)
        })
    
    return result

# Example usage:
# Assuming countries_data is imported or available
# print(most_populated_countries(countries_data, 10))
