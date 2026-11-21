'''Problem q019 (10 minutes)
q019: count_vowels(s) returns how many vowels (a, e, i, o, u)
 are in the string. For now, the string has only small letters.
count_vowels("python") → 1
count_vowels("education") → 5
count_vowels("rhythm") → 0 (tricky: no vowels)
count_vowels("") → 0'''
def count_vowels(s):
    count = 0
    vowels = "aeiou"
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count
print(count_vowels("python"))
print(count_vowels("education"))
print(count_vowels("rhythm"))
print(count_vowels(""))
print(count_vowels("Apple"))

