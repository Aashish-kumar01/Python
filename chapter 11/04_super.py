class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class coder(Employee):
    def __init__(self):
        print("Constructor of Coder")
    b = 2 

class programmer(coder):
    def __init__(self):
        super().__init__()
        print("Constructor of programmer")
    c = 3 

# o = Employee()
# print(o.a)

# o = coder()
# print(o.a, o.b)

o = programmer()
print(o.a, o.b, o.c)
