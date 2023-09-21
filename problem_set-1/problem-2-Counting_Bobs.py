bob_count = 0

for i in range(len(s) - 2):
    if s[i:i+3] == 'bob':
        bob_count += 1

# Print the result
print("Number of times bob occurs is:", bob_count)

