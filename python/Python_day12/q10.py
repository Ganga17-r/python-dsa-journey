#q10-Find the sum of numbers that are greater than 20 but NOT divisible by 5.
numbers = [5, 12, 18, 21, 30, 35, 42, 50]
total=0
for i in range(len(numbers)):
    if numbers[i]>20 and numbers[i]%5!=0:
        continue
    total=total+numbers[i]
print(total)
print("😂"*10)

