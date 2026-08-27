#q4-Find the sum of numbers from 1 to 20, but skip all numbers divisible by 3.
total=0
for i in range(1,21):
    if i%3==0:
        continue
    total=total+i
print(total)