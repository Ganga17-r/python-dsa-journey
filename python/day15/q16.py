'''i = 1 to 5
j = 1 to 5

Print only the pairs where i == j.

Expected output:

1 1
2 2
3 3
4 4
5 5'''
pairs=0
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print(i,j)