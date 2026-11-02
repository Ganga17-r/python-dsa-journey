'''q005: count_positive(nums) returns how many numbers in the list are greater than 0.

count_positive([3, -1, 5, -2, 8]) → 3
count_positive([-4, -7]) → 0
count_positive([]) → 0'''
def count_positive(nums):
        count = 0
        for num in nums:
            if num > 0:
                count =count+ 1
        return count
print(count_positive([3, -1, 5, -2, 8]))
print(count_positive([-4, -7]))     
print(count_positive([]))