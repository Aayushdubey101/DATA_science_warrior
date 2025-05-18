def most_spoken_languages(countries_data, n=10):
    languages_count = {}
    
    for country in countries_data:
        for language in country.get('languages', []):
            if language in languages_count:
                languages_count[language] += 1
            else:
                languages_count[language] = 1
    
    sorted_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]

# Example usage:
# Assuming countries_data is imported or available
# print(most_spoken_languages(countries_data, 10))
