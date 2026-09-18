# find_even(numbers)
numbers = [12, 7, 18, 5, 20, 9, 4]
def even(numbers):
    even_numbers = []
    for n in numbers:
        if n%2==0:
         even_numbers.append(n)
    return even_numbers
print(even(numbers))
