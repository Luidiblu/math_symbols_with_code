x = [1, 2, 3, 4, 5, 6]
result = 0
for i in range(6):
    result += x[i]
print(result)

# Output of print(result) -> 21

x = [1, 2, 3, 4, 5, 1]
result = 1
for i in range(6):
    result *= x[i]
print(result)
# Output of print(result) -> 120