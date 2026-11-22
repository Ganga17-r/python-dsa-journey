# My Progress

## Revision R1
- Functions: is_even, largest_of_three, grade
- Bug found: > vs >= when numbers are equal
- Git: status, add, commit, push

## Revision R2
- q004 sum_list, q005 count_positive, q006 find_smallest
- q007 count_even (a helper function inside another function)
- q008 average
- q009 second_largest
- Bug found: wrong starting value of `second` hid the bug, and I fixed it with None
- q010 second_smallest (same idea as q009, signs flipped)
- Fixed the average function name and variable
-q011-A bad pair means we can say False at once. But “True” needs every pair checked.
- q013 reverse_list: swapping with a, b = b, a; right = len(nums) - 1 - i; loop only len(nums) // 2 times
- Learned: = works out the right side first, then puts values in the left side
-q014-The order of lines matters. Count only after the work is done.
-q015a,q015b-- q014 move_zeros, q015 insert_at and delete_at: insert shifts items right, pop shifts items left; check pos before pop.Insert shifts items to the right. Delete shifts items to the left.
-q016 index_of_max: use > (not >=) so the first largest stays.
-q017-- reverse_string: strings cannot be changed in place, so build a new string with result = ch + result
- Python: slicing [start:stop], upper(), lower(), + joins stringsa string cannot be changed in place
-- q018 is_palindrome: reverse the string, then compare with ==; capital and small letters are different
- Learned: s[::-1] is a shortcut for reversing, but I wrote the long way first
- q019 count_vowels: loop through the string, use "in" to check each character, count grows by 1
- Learned: "a" in "cat" gives True or False
- q020 count_digits: same counting pattern, new check with isdigit()
-- q021 first_digit_position: return position inside the loop when found, return -1 after the loop when not found
- [x] Strings (basics): reverse, palindrome, count_vowels, count_digits, first_digit_position
## Learned
- return delivers a value, the condition decides True or False
- test the tricky cases (equal numbers, empty list)
- Git: status, add, commit, push

## Next
- Fix the average function name, then q010
- Fixed my GitHub connection problem: restart laptop and phone, then reconnect
## DSA Topic Tracker
- [x] Arrays
- [x] Strings (basics): reverse, palindrome, count_vowels, count_digits, first_digit_position
- [ ] Sorting
- [ ] Hashing (counting)
- [ ] Stack and Queue
- [ ] Linked list
- [ ] Recursion
