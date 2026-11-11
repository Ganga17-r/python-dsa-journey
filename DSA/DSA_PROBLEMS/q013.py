'''#Reversing array
#problem-1
nums=[1,2,3,4,5]
nums[0],nums[4]=nums[4],nums[0]
nums[1],nums[3]=nums[3],nums[1]
print(nums)
#problem-2
nums=[1,2,3,4,5,6]
nums[0],nums[5]=nums[5],nums[0]
nums[1],nums[4]=nums[4],nums[1]
nums[2],nums[3]=nums[3],nums[2]
print(nums)
'''
'''Problem q013

q013: reverse_list(nums) reverses the list in place and returns it. Do not use reverse(), [::-1], or reversed(). Use swapping.

reverse_list([1, 2, 3, 4]) → [4, 3, 2, 1]
reverse_list([1, 2, 3, 4, 5]) → [5, 4, 3, 2, 1]
reverse_list([7]) → [7]
reverse_list([]) → []'''
def  reverse_list(nums):
    for i in range(len(nums)//2):
        right=len(nums)-1-i
        nums[i], nums[right] = nums[right], nums[i]
    return nums
print(reverse_list([1, 2, 3, 4]))
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list([7]))
print(reverse_list([]))
    


