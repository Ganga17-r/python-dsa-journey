'''q010: second_smallest(nums) returns the second smallest number 
in the list. You can assume the list has at least 2 different
 numbers.

second_smallest([4, 9, 2, 7]) → 4
second_smallest([5, 1]) → 5
second_smallest([2, 2, 8]) → 8 (tricky: the smallest is repeated)'''
def second_smallest(nums):
    smallest= nums[0]
    second = None

    for num in nums:
        if num < smallest:
            second = smallest
            smallest = num

        elif second is None or num < second:
            if num >smallest:
                second = num

    return second


print(second_smallest([4, 9, 2, 7]))
print(second_smallest([5, 1]) )
print(second_smallest([2, 2, 8]) )
print(second_smallest([3, 1, 1]))
print(second_smallest([1, 2, 2]))