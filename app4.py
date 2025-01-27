import hashlib

def transform_string(myString):
    ascii_codes = [ord(char) for char in myString]
    print(ascii_codes)
    num_char = len(ascii_codes)
    print(num_char)
    multiplied_values = (val * num_char for val in ascii_codes)
    print(multiplied_values)
    total_sum = sum(multiplied_values)
    print(total_sum)
    hash_object = hashlib.sha256(str(total_sum).encode())
    hash_String = hash_object.hexdigest()
    return hash_String

myString = "CitricSheep"
print(transform_string(myString))