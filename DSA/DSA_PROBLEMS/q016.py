'''q016: position of the largest number
q016: index_of_max(nums) returns the position 
(not the value) of the largest number. If the largest number 
appears more than once, return the first position.
Do not use max() or index().
index_of_max([4, 9, 2, 7]) → 1
index_of_max([-5, -2, -9]) → 1
index_of_max([6]) → 0
index_of_max([3, 8, 8, 1]) → 1 
(tricky: the largest is repeated, so return the first position'''
def index_of_max(nums):
    largest=nums[0]
    max_index=0
    for i in range(len(nums)):
        if nums[i]>largest:
            largest=nums[i]
    return largest
print(index_of_max([4, 9, 2, 7]))
print(index_of_max([-5, -2, -9]))
print(index_of_max([6]))
print(index_of_max([3, 8, 8, 1]))
