marks = {
    "Aashish": 93,
    "Abhishek": 84,
    "Ankit": 91,
    0: "Harry"
}

# print(marks.items())
print(marks.keys())
# print(marks.values())
# marks.update({"Aashish": 53, "Rohan": 28} )
# print(marks)

# print(marks.get("Aashish")) # print the value assigned to key "Aashish" or print none if the key is not in the dictionary
# print(marks["Aashish"]) # returns an error if the key "Aashish" is not available in the dictionary otherwise print the value assigned to the key 


# These are the methods of dictionary
# print(marks.pop("Aashish")) # removes the key "Aashish" from the dictionary and returns its value

print(marks.popitem()) # removes the last inserted key-value pair from the dictionary and returns it as a tuple

# print(marks.clear()) # removes all the elements from the dictionary

# marks2 = marks.copy() # creates a shallow copy of the dictionary

# print(marks.fromkeys(["Aashish", "Abhishek"])) # creates a new dictionary with the given keys and values as None

# print(marks.setdefault("Aashish")) # returns the value of the key "Aashish" if it is in the dictionary, otherwise inserts the key with a value of None and returns None

print(marks.setdefault("Rohan", 45)) # returns the value of the key "Rohan" if it is in the dictionary, otherwise inserts the key with a value of 45 and returns 45

print(marks)
