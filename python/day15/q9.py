'''Q9 — Nested Loops + Conditional Sum-Calculate the sum of only the even values of i + j.
Using:

i = 1 to 4
j = 1 to 3'''
total=0
for i in range(1,5):
    for j in range(1,4):
        if (i+j)%2==0:
            total=total+(i+j)
print(total)

