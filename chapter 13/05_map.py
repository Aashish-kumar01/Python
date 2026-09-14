from functools import reduce

# Map function 
l = [1, 2, 3, 4, 5]
square = lambda X:X*X
squarelist = map(square, l)
print(list(squarelist))


# Filter function
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyeven = filter(even, l)
print(list(onlyeven))
# print(list(filter(even, l)))


# Reduce function

def sum(a,b):
    return a + b
print(reduce(sum,l))
