# num = [12, 25, 7, 45, 18, 30, 9, 50]
# Find the smallest number greater than 20.
# Expected output:25
num = [12, 25, 7, 45, 18, 30, 9, 50]
smallest=num[1]
for i in range(len(num)):
    if num[i]>20 and num[i]<smallest:
     smallest=num[i]
print(smallest)
