'''q008: average(nums) returns the average of the numbers. 
The average is the sum divided by how many numbers.
 Use sum_list inside it. If the list is empty, return 0.

average([2, 4, 6]) → 4.0
average([5]) → 5.0
average([]) → 0'''
def sum_list(nums):
     total = 0
     for num in nums:
        total =total+ num
     return total
def average(nums):
    
    if len(nums) == 0:
        return 0        
    else:
        result = sum_list(nums)/len(nums)
        return result
print(average([2, 4, 6]))
print(average([5]) )
print(average([]))