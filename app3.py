import hashlib

def string_transform(the_string):
    ascii_values = [ord(char) for char in the_string]
    print(ascii_values)
    num_char = len(the_string)
    print(num_char)
    multiplied_values = [value * num_char for value in ascii_values]
    print(multiplied_values)
    total_sum = sum(multiplied_values)
    print(total_sum)
    hash_object = hashlib.sha256(str(total_sum).encode())
    hash_string = hash_object.hexdigest()
    return hash_string

myString = "Jessica Miramontes"
print(string_transform(myString))

# Inverse string
inversed = myString[::-1]
print(inversed)

change_vocals = {'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5'}
transformed_string = ''.join(change_vocals.get(char,char) for char in myString)
print(transformed_string)

only_vocals = ''.join(filter(lambda x: x in "aeiouAEIOU", myString))
print(only_vocals)
print(myString.split(' '))