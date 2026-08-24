# Find the sum of all ODD numbers from 1 to 20.
total=0
for i in range(1,21):
    if i%2!=0:
        total=total+i
print(total)