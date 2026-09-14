s = {}

name = input("Enter your name: ")
lan = input("Enter your language: ")
s[name] = lan
name = input("Enter your name: ")
lan = input("Enter your language: ")
s[name] = lan
name = input("Enter your name: ")
lan = input("Enter your language: ")
s[name] = lan
name = input("Enter your name: ")
lan = input("Enter your language: ")
s[name] = lan

print(s)


# Alternative way to do the same thing using update method of dictionary
s = {}

name = input("Enter your name: ")
lan = input("Enter your language: ")
s.update({name: lan}) # It will update the dictionary s with the key value pair name: lan , if the key is already present it will update its value otherwise it will add the key value pair to the dictionary
print(s)