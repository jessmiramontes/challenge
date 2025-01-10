import hashlib

# Initialize variable
myString = "CitricSheep"

# Get the ASCII values
ascii_values = [ord(char) for char in myString]

# Multiply each value by the number of characters in the string
num_chars = len(myString)
multipliend_values = [value * num_chars for value in ascii_values]

# Sum the values
total_sum = sum(multipliend_values)

# Generate a SHA256 hash of this sum
hash_object = hashlib.sha256(str(total_sum).encode())
hex_string = hash_object.hexdigest()

#Print the hexadecimal string
print(hex_string)