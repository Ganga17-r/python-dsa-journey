'''Problem q020
This is the count_vowels pattern, with a new check.
q020: count_digits(s) returns how many digits (0 to 9) 
are in the string.
count_digits("abc123") → 3
count_digits("python") → 0
count_digits("r2d2") → 2
count_digits("2026") → 4
count_digits("") → 0 (tricky: an empty string)'''
def count_digits(s):
    count=0
    for ch in s:
        if ch.isdigit():
            count=count+1
    return count
print(count_digits("abc123"))
print(count_digits("python"))
print(count_digits("r2d2"))
print(count_digits("2026"))
print(count_digits("")) 


