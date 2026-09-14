class calculator:
    n = 10
    m = 15
    o = 196

    @staticmethod
    def greet():
        print("Hello")
    def calculate(self):
        print(f"The square of the number {self.n}: {self.n**2}")
        print(f"The cube of the number {self.m}: {self.m**3}")
        print(f"The square root of the number {self.o}: {self.o**0.5}")

number = calculator()
number.greet()
number.calculate()

