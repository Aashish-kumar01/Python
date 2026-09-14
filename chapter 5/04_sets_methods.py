s = {1, 34, 24, 643, 5, 63, "Aashish"}

print(s, type(s))

s.add(45) # It will add the element to the set
print(s, type(s))

s.remove(63) # It will give an error if the element is not present in the set otherwise it will remove the element
print(s, type(s))

s.pop() # It will remove a random element from the set
print(s, type(s))