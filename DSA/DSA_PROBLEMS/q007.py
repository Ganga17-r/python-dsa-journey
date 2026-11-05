'''q007: count_even(nums) returns how many even numbers are in the
 list. Use is_even inside it.

count_even([1, 2, 4, 7, 8]) → 3
count_even([3, 5, 9]) → 0
count_even([]) → 0'''
def is_even(n):
    return n % 2 == 0
def count_even(nums):
    count = 0
    for n in nums:
        if is_even(n):
            count =count+1
    return count
print(count_even([1, 2, 4, 7, 8]) )
print(count_even([3, 5, 9]) )
print(count_even([]) )