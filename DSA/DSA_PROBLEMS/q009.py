'''q009: second_largest(nums) returns the second biggest 
    number in the list. You can assume the list has
      at least 2 different numbers.

second_largest([4, 9, 2, 7]) → 7
second_largest([5, 1]) → 1
second_largest([8, 8, 3]) → 3 (tricky: the biggest is repeated)'''


def second_largest(nums):
    largest = nums[0]
    second = None

    for num in nums:
        if num > largest:
            second = largest
            largest = num

        elif second is None or num > second:
            if num < largest:
                second = num

    return second


print(second_largest([4, 9, 2, 7]))
print(second_largest([5, 1]))
print(second_largest([8, 8, 3]))
 