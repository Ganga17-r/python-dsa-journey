# Count numbers less than 20
# given:numbers = [12, 25, 7, 45, 18, 30, 9, 50]
num = [12, 25, 7, 45, 18, 30, 9, 50]
count=0
for i in range(len(num)):
    if num[i]<20:
        count=count+1
print(count)