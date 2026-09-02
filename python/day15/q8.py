'''# Q8 — Nested Loops + Sum
Using nested loops, calculate the sum of all values of i + j.

Use:

i = 1 to 3
j = 1 to 2'''
total=0
for i in range(1,4):
    for j in range(1,3):
         total=total+(i+j)
print(total)