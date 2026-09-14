a = 43

def fun():
    global a
    a = 3
    print(a)

print(a)
fun()