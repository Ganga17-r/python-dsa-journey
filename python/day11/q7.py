# Find the smallest number in this list:
# numbers = [12, 45, 7, 89, 23, 56]
num = [12, 45, 7, 89, 23, 56]
smallest=num[0]
for i in range(len(num)):
    if num[i]<smallest:
        smallest=num[i]
print(smallest)