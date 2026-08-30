num = [12, 7, 18, 25, 31, 42, 55, 60]

#Find the first number that is:
'''greater than 20 AND divisible by 5'''
for i in range(len(num)):
    if num[i]>20 and num[i]%5==0:
          print('First matching number:',num[i])
          break
else:
   print('No matching number found')