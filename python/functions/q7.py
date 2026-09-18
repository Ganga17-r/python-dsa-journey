# min_max(numbers) function.
numbers = [18, 5, 27, 11, 3, 20]
def mim_max(numbers):
 largest=numbers[0]
 smallest=numbers[0]
 for n in numbers:
    if n>largest:
        largest=n
    if n<smallest:
        smallest=n
 return smallest,largest
result = mim_max(numbers)
print(result)
