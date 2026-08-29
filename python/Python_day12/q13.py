#13q-Find the largest number that is NOT divisible by 5.
num = [15, 22, 7, 30, 11, 40, 9, 26]
largest=num[1]
for i in range(len(num)):
    if num[i]>largest and num[i]%5!=0:
        largest=num[i]
print(largest)
