#Q10 — Now YOU choose the logic

num= [4, 9, 12, 18, 25, 31, 40, 47]

#Find the first number that is greater than 20 and divisible by 2.

for i in range(len(num)):
    if num[i]>20 and num[i]%2==0:
        print('First matching number:',num[i])
        break
else:
 print('No matching number found')