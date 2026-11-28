'''Problem q023
This is a linear search, and you already know 
every piece from q021.
q022: linear_search(nums, target) returns the 
position of target in the list. If it is not there, 
return -1. Do not use index() or in.
linear_search([5, 8, 3, 9], 8) → 1
linear_search([4, 9, 7, 2], 7) → 2
linear_search([6], 6) → 0
linear_search([1, 2, 3], 10) → -1 (not found)
linear_search([], 5) → -1 (tricky: an empty list)
linear_search([3, 7, 3], 3) → 0
(tricky: the target appears twice, so return the first position)'''
def linear_search(nums,target):
    position=0
    for n in nums:
        if n==target:
            return position
        position=position+1
    return -1
print(linear_search([5, 8, 3, 9], 8))
print(linear_search([4, 9, 7, 2], 7))
print(linear_search([6], 6))
print(linear_search([1, 2, 3], 10))
print(linear_search([], 5))
print(linear_search([3, 7, 3], 3))

   
