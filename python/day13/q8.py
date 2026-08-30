# Q8 — First number divisible by BOTH 3 and 5

numbers = [7, 12, 18, 25, 30, 42, 50]
for i in range(len(numbers)):
    if numbers[i]%3==0 and numbers[i]%5==0:
     print('First number divisible by both:',numbers[i])
     break
else:
     print('No matching number found')