'''q012: has_equal_neighbours(nums) returns True if any two 
neighbouring numbers are equal, 
otherwise False.

has_equal_neighbours([1, 2, 2, 5]) → True
has_equal_neighbours([1, 2, 3]) → False
has_equal_neighbours([7]) → False
has_equal_neighbours([1, 2, 1, 2]) → False 
(tricky: the numbers repeat, but they are not neighbours)'''
def has_equal_neighbours(nums):
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False
print(has_equal_neighbours([1, 2, 2, 5])) 
print(has_equal_neighbours([1, 2, 3]))
print(has_equal_neighbours([7]))
print(has_equal_neighbours([1, 2, 1, 2]))