# Find the largest number in this list:
# numbers = [12, 45, 7, 89, 23, 56]
num = [12, 45, 7, 89, 23, 56]
largest=num[0]
for i in range(len(num)):
    if num[i]>largest:
        largest=num[i]
print(largest)