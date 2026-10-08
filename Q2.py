sentence = input("Enter a sentence: ")

num_chars = len(sentence)
num_words = len(sentence.split())
num_spaces = sentence.count(" ")

vowels = "aeiouAEIOU"
num_vowels = 0
num_digits = 0

for ch in sentence:
    if ch in vowels:
        num_vowels += 1
    if ch.isdigit():
        num_digits += 1

print("Number of characters:", num_chars)
print("Number of words:", num_words)
print("Number of vowels:", num_vowels)
print("Number of spaces:", num_spaces)
print("Number of digits:", num_digits)
