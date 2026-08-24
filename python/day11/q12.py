# num = [12, 25, 7, 45, 18, 30, 9, 50]
# Find the largest number greater than 20.
# Expected output:50
num = [12, 25, 7, 45, 18, 30, 9, 50]
largest=num[0]
for i in range(len(num)):
    if num[i]>20 and num[i]>largest:
     largest=num[i]
print(largest)
