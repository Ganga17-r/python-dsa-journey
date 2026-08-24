# Find how many EVEN numbers are present from 1 to 20.
count=0
for i in range(1,21):
    if i%2==0:
        count=count+1
print(count)