# Practice 4 — sum_even(numbers)

def sum_even(num):
    total=0
    for n in num:
     if n%2==0:
        total=total+n
    return total
    
num = [10, 7, 4, 13, 20, 9]
print(sum_even(num))