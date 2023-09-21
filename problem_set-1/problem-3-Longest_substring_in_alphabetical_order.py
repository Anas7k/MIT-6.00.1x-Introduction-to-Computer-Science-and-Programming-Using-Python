current_substring = s[0]
longest_substring = s[0]
for i in range(1, len(s)):
    if s[i] >= current_substring[-1]:
        current_substring += s[i]
    else:
        current_substring = s[i]
   
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

print("Longest substring in alphabetical order is:", longest_substring)

