# num = [5, 12, 25, 45, 18, 30, 9, 50, 35]

# Count how many numbers are:

# greater than or equal to 10 AND less than or equal to 40
num = [5, 12, 25, 45, 18, 30, 9, 50, 35]
count=0
for i in range(len(num)):
    if num[i]>=10 and num[i]<=40:
        count=count+1
print(count)
