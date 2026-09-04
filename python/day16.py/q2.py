# '''Q2-Find the sum of all even numbers
numbers= [12, 7, 18, 5, 20, 9]
total=0
for num in numbers:
    if num%2==0:
        total=total+num
print(total)
