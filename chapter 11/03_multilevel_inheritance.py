# class Employee:
#     company = "ITC"
#     name = "Aashish"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the company is {self.company}")


# class coder(Employee):
#     language = "Javascript"
#     name = "Rohan"
#     def printlanguage(self):
#         print(f"The language is {self.language}")


# class programmer(coder):
#     company = "ITC Infotech"
#     name = "Abhishek"
#     language = "Python"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

# b = programmer()
# b.printlanguage()
# b.show()
# b.showLanguage()


class Employee:
    a = 1

class coder(Employee):
    b = 2 

class programmer(coder):
    c = 3 

o = Employee()
print(o.a)
o = programmer()
print(o.a, o.b, o.c)
