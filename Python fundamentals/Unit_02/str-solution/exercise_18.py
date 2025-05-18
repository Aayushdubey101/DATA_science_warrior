# Exercise 18: Create an acronym or an abbreviation for the name 'Python For Everyone'.

phrase = "Python For Everyone"
words = phrase.split()
acronym = "".join(word[0].upper() for word in words)
print(acronym)  # Output: PFE
