# Exercise 19: Create an acronym or an abbreviation for the name 'Coding For All'.

phrase = "Coding For All"
words = phrase.split()
acronym = "".join(word[0].upper() for word in words)
print(acronym)  # Output: CFA
