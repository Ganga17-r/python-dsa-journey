#q5-Count how many numbers from 1 to 30 are NOT divisible by 4.
count=0
for i in range(1,31):
    if i%4==0:
        continue
    count=count+1
print(count)