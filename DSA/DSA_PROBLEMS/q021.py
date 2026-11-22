'''q021: position of the first digit
q021: first_digit_position(s) returns the position of the first digit in the string. If there is no digit, return -1.
first_digit_position("abc123") → 3
first_digit_position("a1b2") → 1
first_digit_position("2026") → 0
first_digit_position("python") → -1
first_digit_position("") → -1 (tricky: an empty string)'''
def first_digit_position(s):
    position=0
    for ch in s:
        if ch.isdigit():
           return position
        position=position +1
    return -1
print(first_digit_position("abc123"))
print(first_digit_position("a1b2"))
print(first_digit_position("2026"))
print(first_digit_position("python"))
print(first_digit_position(""))
