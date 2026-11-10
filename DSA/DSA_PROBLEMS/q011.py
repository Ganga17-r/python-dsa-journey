'''q011: is_sorted(nums) returns True if the numbers are in 
increasing order (small to big), otherwise False.

is_sorted([1, 3, 5, 8]) → True
is_sorted([1, 5, 3, 8]) → False
is_sorted([4]) → True
is_sorted([2, 2, 5]) → True (equal numbers are okay)'''
def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True
print(is_sorted([1, 3, 5, 8])) 
print(is_sorted([1, 5, 3, 8]) )
print(is_sorted([4]))
print(is_sorted([2, 2, 5]))