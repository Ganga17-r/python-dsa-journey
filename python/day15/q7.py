# Q7: Nested Loops + Counting
# Using nested loops, count how many pairs (i, j) have an even sum.
count=0
for i in range(1,5):
    for j in range(1,4):
        if (i+j)%2==0:
            count=count+1
print(count)