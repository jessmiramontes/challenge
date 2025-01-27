import hashlib

myString = "CitricSheep"
ascii_values = [ord(char) for char in myString]
print(ascii_values)
num_char = len(myString)
print(num_char)
multiplied_values = [value * num_char for value in ascii_values]
total_sum = sum(multiplied_values)
print(total_sum)
hash_object = hashlib.sha256(str(total_sum).encode())
hash_string = hash_object.hexdigest()
print(hash_string)
