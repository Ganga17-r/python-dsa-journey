"""Q5 — Nested loop + condition

Write a program using nested loops to print only the even values of j:

1 2
2 2
3 2
4 2"""
for i in range(1,5):
    for j in range(1,3):
        if j%2==0:
            print(i,j)