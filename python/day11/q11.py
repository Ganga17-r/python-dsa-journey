# Q11— Sum numbers less than 20
num = [12, 25, 7, 45, 18, 30, 9, 50]
total=0
for i in range(len(num)):
    if num[i]<20:
        total=total+num[i]
print(total)
