'''Problem q018
q018: is_palindrome(s) returns True if the string reads
the same forwards and backwards, otherwise False. 
Use your reverse_string inside it.
is_palindrome("madam") → True
is_palindrome("python") → False
is_palindrome("a") → True
is_palindrome("") → True (an empty string reads the same both 
                          ways)
is_palindrome("Madam") → 
False (tricky: capital M and small m are different,
        so for now we do not change the case)'''
#def is_palindrome(s):
    #return s == s[::-1]
def reverse_string(word):
     result=""
     for ch in word:
          result=ch+result
     return result                    # your q017 code

def is_palindrome(s):
    rev = reverse_string(s)
               
    return rev==s             # compare s with rev
print(is_palindrome("madam"))
print(is_palindrome("python"))
print(is_palindrome("a"))
print(is_palindrome(""))
print(is_palindrome("Madam"))