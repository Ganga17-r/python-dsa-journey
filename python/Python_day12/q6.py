#q6-Find the sum of all ODD numbers from 1 to 30, but use continue to skip the even numbers.
sum=0
for i in range(1,31):
    if i%2==0:
        continue
    sum=sum+i

print(sum)