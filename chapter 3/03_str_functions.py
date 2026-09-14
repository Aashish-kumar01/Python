name = "Aashish"

print(len(name))
print(name.endswith("sh"))
print(name.count("a"))
print(name.capitalize())
print(name.find("shi"))
print(name.replace("Aashish", "CodeWithHarry"))
print(name*3)  # This will print the string 3 times
print(name.lower())
print(name.upper())
print(name.title())  # This will convert the first letter of each word to uppercase
print(name.isdigit())  # This will check if all the characters in the string are digits
print(name.isalpha())  # This will check if all the characters in the string are alphabets
print(name.index("s"))  # This will give the index of the first occurrence of the character
print(name.swapcase())  # This will swap the case of each character in the string
print(name.split("a"))  # This will split the string at each occurrence of the character and return a list
print(name.find("x"))  # This will return -1 if the character is not found in the string
print(name.center(20, '*'))  # This will center the string in a field of given width and fill with specified character
print(name.encode())  # This will encode the string to bytes
print(name.endswith("h", 5, 8))  # This will check if the string ends with the specified suffix in the given range
print(name.islower())  # This will check if all the characters in the string are lowercase
print(name.istitle())  # This will check if the string is in title case
print(name.isspace())  # This will check if all the characters in the string are whitespace
print(name.lstrip("Aa"))  # This will remove the specified characters from the left side of the string
print(name.rstrip("sh"))  # This will remove the specified characters from the right side of the string
