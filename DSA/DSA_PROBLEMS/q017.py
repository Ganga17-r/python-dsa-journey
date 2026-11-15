'''word='cat'
for i in range(len(word)):
    print(i,word[i])
#slicing
word = "python"

print(word[:3])     # pyt   (from the beginning, stop before 3)
print(word[3:])     # hon   (from position 3, to the end)
print(word[:])      # python (the whole string)
print(word[2:])
print(word.lower())
print(word.upper())
word="python"
result=""
for ch in word:
    result=ch+result
print(result)
'''
"""Problem q017

q017: reverse_string(s) returns the string reversed. 
Do not use [::-1] or reversed().
 Build the new string with a loop.
reverse_string("python") → "nohtyp"
reverse_string("hi") → "ih"
reverse_string("a") → "a"
reverse_string("") → "" (tricky: an empty string)"""
def reverse_string(word):
    result=""
    for ch in word:
        result= ch + result
    return result
print(reverse_string("python"))
print(reverse_string("hi"))
print(reverse_string("a"))
print(reverse_string(""))
