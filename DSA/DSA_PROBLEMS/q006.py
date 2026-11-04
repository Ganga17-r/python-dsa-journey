'''q006: find_smallest(nums) returns the smallest number in 
the list. Do not use min().

find_smallest([4, 9, 2, 7]) → 2
find_smallest([-5, -2, -9]) → -9
find_smallest([6]) → 6'''


def find_smallest(nums):
    smallest = nums[0]

    for n in range(len(nums)):
        if nums[n] < smallest:
            smallest = nums[n]

    return smallest

print(find_smallest([4, 9, 2, 7]))
print(find_smallest([-5,-2,-9]))
print(find_smallest([6]))