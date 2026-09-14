s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 
# s.add(23.4)

print(len(s))
print(s)

# Amswer is 2 because 20 and 20.0 are considered the same in a set as they have the same hash value.

