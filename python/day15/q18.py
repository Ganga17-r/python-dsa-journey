'''Q18 — the final challenge 🔥

Using:

i = 1 to 5
j = 1 to 5

Find the sum of all pairs where i + j > 6.'''
total=0
for i in range(1,6):
    for j in range(1,6):
        if i+j>6:
            total=total+(i+j)
print(total)