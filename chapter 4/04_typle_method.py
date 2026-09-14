a = (1, 23, 335, "Aashish", 23, 23.4, False, "Abhishek") # Tuple is immutable (cannot be changed)

print(a)

no = a.count(23)
print(no)
index = a.index("Aashish")
print(index)
print(type(a))
t = a.index(23, 1, 4)
print(t)

print(len(a))


