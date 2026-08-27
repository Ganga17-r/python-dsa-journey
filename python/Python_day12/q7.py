#q7-Print numbers from 1 to 30 that are divisible by 2 OR 5, 
# but skip numbers that are divisible by BOTH 2 AND 5.
for i in range(1,31):
    if i%2==0 and i%5==0:
        continue
    if i%2==0 or i%5==0:
        print(i)