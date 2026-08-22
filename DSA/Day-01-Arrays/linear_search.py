# Day 1 - Arrays
# Problem: Linear Search

arr = [4, 1, 7, 9, 2]
target = 7
found = False

for num in arr:
    if num == target:
        found = True
        break

print("Found:", found)