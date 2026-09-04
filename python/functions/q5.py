# largest(numbers)
def largest(number):
    largest=number[0]
    for n in number:
        if n>largest:
            largest=n
    return largest
number = [12, 45, 7, 31, 28]
print(largest(number))