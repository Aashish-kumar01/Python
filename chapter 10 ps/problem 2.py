

class calculator:
    n = 10
    m = 15
    o = 196
    def calculate(self):
        print(f"The square of the number {self.n}: {self.n**2}")
        print(f"The cube of the number {self.m}: {self.m**3}")
        print(f"The square root of the number {self.o}: {self.o**0.5}")

number = calculator()
number.calculate()






# Another way to do this problem
# class calculator:
#     def __init__(self, n, m, o):
#         print(f"The square of the number {n}: {n*n}")
#         print(f"The cube of the number {m}: {m**3}")
#         print(f"The square root of the number {o}: {o**0.5}")

# number = calculator(10, 15, 196)




# Another way to do the same thing
# class cal:
#     def __init__(self, n):
#         self.n = n
#     def square(self):
#         print(f"The square of the number {self.n}: {self.n*self.n}")
#     def cube(self):
#         print(f"The cube of the number {self.n}: {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"The square root of the number {self.n}: {self.n**0.5}")

# num = cal(4)
# num.square()
# num.cube()
# num.squareroot()
        

