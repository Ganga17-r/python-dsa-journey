#Create:
#It should return three things:

# Largest number
# Smallest number
# Average
numbers = [10, 25, 7, 40, 18]
def analyze(numbers):
 largest=numbers[0]
 smallest=numbers[0]
 total=0
 for n in numbers:
  total=total+n
  if n>largest:
   largest=n
  if n<smallest:
    smallest=n
 average = total / len(numbers)
 return average,largest,smallest
average, largest, smallest = analyze(numbers)
print(analyze(numbers))
