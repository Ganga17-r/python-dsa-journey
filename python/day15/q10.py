'''Q10 — Nested Loops + Counting Specific Pairs
Using:

i = 1 to 5
j = 1 to 5

Count how many pairs satisfy:

i > j'''
count=0
for i in range(1,6):
    for j in range(1,6):
        if i>j:
            count=count+1
print(count)