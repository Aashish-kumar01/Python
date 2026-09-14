from functools import reduce
l = [328,3923932,23,232,32,2323,3223]

def greatestno(a, b):
    if (a>b):
        return a
    return b

print(reduce(greatestno, l))