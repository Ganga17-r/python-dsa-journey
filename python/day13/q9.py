#Q9 — First number satisfying a condition

num = [11, 17, 23, 29, 35, 41, 47]

#Find the first number greater than 20 AND odd.
for i in range(len(num)):
    if num[i]>20 and num[i]%2!=0:
        print('First matching number:',num[i])
        break
else:
    print('No matching number found')