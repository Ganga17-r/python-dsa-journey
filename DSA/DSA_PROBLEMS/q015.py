'''Problem q015
Use insert() and pop() for two small functions.
q015a: insert_at(nums, pos, value) inserts value at position pos,
 and returns the list.
insert_at([1, 2, 4], 2, 3) → [1, 2, 3, 4]
insert_at([5, 6], 0, 4) → [4, 5, 6]
insert_at([1, 2], 2, 3) → [1, 2, 3] (tricky: insert at the end)
insert_at([](, 0, 9) → [9]'''
def insert_at(nums,pos,value):
    nums.insert(pos,value)
    return nums
print(insert_at([1, 2, 4], 2, 3))
print(insert_at([5, 6], 0, 4))
print(insert_at([1, 2], 2, 3))
print(insert_at([],0, 9))
'''q015b: delete_at(nums, pos) removes the item at position pos, and returns the list.

delete_at([1, 2, 3, 4], 1) → [1, 3, 4]
delete_at([5], 0) → []
delete_at([7, 8, 9], 2) → [7, 8] (the last item)'''
def delete_at(nums,pos):
     if pos < 0 or pos >= len(nums):
        return nums
     nums.pop(pos)
     return nums
print(delete_at([1, 2, 3, 4], 1))
print(delete_at([5], 0))
print(delete_at([7, 8, 9], 2))
print(delete_at([1, 2, 3], 5))
print(delete_at([1, 2, 3], -1))