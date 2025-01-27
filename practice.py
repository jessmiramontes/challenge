"""
Given a string, write a function named rearrange_string that performs the following:
Removes all digits.
Converts all uppercase letters to lowercase.
Reverses the string.
"""

def rearrange_string(myString):
    string_no_digits =  ''.join(filter(lambda x: not x.isdigit(), myString))
    print(string_no_digits)
    string_no_digits = string_no_digits.lower()
    string_reversed = string_no_digits[::-1]
    return string_reversed

myString = "AbC123DeF"
result = rearrange_string(myString)
print("terminado")
print(result)