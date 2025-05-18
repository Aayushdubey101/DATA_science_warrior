# Exercise 27: Slice out the phrase 'because because because' in the sentence.

sentence = 'You cannot end a sentence with because because because is a conjunction'
start = sentence.find('because')
end = start + len('because because because')
new_sentence = sentence[:start] + sentence[end:]
print(new_sentence.strip())  # Output: You cannot end a sentence with is a conjunction
