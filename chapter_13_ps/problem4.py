l = [6, 2, 5, 15, 20, 25, 34, 53, 23, 45]

def mul(n):
    if (n%5 == 0):
        return True
    return False

f = list(filter(mul, l))
print(f)