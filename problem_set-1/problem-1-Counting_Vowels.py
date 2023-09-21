vowel_count = 0

valid_vowels = ['a', 'e', 'i', 'o', 'u']

for char in s:
    if char in valid_vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)

