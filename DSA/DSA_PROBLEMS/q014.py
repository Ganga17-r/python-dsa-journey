'''q014: move_zeros(nums) returns a new list with 
all zeros moved to the end. The other numbers must stay in the
 same order.
move_zeros([0, 1, 0, 3, 12]) → [1, 3, 12, 0, 0]
move_zeros([0, 4, 0, 5, 7]) → [4, 5, 7, 0, 0]
move_zeros([1, 2, 3]) → [1, 2, 3] (no zeros)
move_zeros([0, 0]) → [0, 0] (all zeros)
move_zeros([]) → []'''
def move_zeros(nums):
    result=[]
    
    for n in nums:
        if n!=0:
            result.append(n)
    missing=len(nums)-len(result)
    for n in range(missing):
      result.append(0)
    return result

    
print(move_zeros([0,2,3,4,0]))
print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([0, 4, 0, 5, 7]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0]))
print(move_zeros([]))
            
    
        