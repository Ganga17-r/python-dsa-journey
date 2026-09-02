"""Q6 —Write a nested-loop program to print only values where i + j is even.

For:

i = 1 to 4
j = 1 to 3

Expected output:

1 1
1 3
2 2
3 1
3 3
4 2"""
for i in range(1,5):
    for j in range(1,4):
        if (i+j)%2==0:
         print(i,j)