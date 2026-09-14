class Employee:
    salary = 230000
    # increment = 50
    # def __init__(self):
    #     print(f"The salary is {self.salary}")
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = (((salary/self.salary) - 1)*100) # *salary 

    # def __mul__():



e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 345000
print(e.increment)


