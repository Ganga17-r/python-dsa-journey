# BINARY SEARCH
#
# Binary Search works only on a sorted array.
#
# Basic idea:
# 1. Look at the middle.
# 2. Compare middle with target.
# 3. If target == middle → FOUND.
# 4. If target < middle → go LEFT.
# 5. If target > middle → go RIGHT.
#
# Binary Search eliminates half of the search area
# after each comparison.
#
# Variables:
# low  → first index of current search area
# high → last index of current search area
# mid  → middle index
#
# Rules:
# target == arr[mid] → FOUND
# target < arr[mid]  → high = mid - 1
# target > arr[mid]  → low = mid + 1
#
# Middle:
# mid = (low + high) // 2
#
# Important:
# // is floor division.