"""#'' Q17 — Nested Loops + Condition + Accumulator. 😎🔥

Using:

i = 1 to 5
j = 1 to 5

Count how many pairs satisfy:

i + j > 6''"""
count=0
for i in range(1,6):
    for j in range(1,6):
        if i+j>6:
            count=count+1
print(count)
