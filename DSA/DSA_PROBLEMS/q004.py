'''q004: sum_list(nums) returns the sum of all numbers in the list. Do not use sum().

sum_list([1, 2, 3, 4]) → 10
sum_list([5]) → 5
sum_list([]) → 0'''
def sum_list(nums):
    total = 0
    for num in nums:
        total =total+ num
    return total
print(sum_list([1,2,3,4]))
print(sum_list([5]))
print(sum_list([]))