# Find how many ODD numbers are present from 1 to 30.
count=0
for i in range(1,31):
    if i%2!=0:
        count=count+1
print(count)