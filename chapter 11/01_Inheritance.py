class Employee:
    company = "ITC"
    name = "Aashish"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")


# class programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the company is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


class programmer(Employee):
    # company = "ITC Infotech"
    # name = "Abhishek"
    language = "Python"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = programmer()
a.company = "Infosys"
b.company = "Microsoft"
a.show() # This will check the instance attribute of a if not available then go through the class attribute
print(a.company, b.company)
# a.show()

b.show() # This will check the instance attribute of b if not available then go through the class attribute of b if that is also not available then go through the class attribute of a but won't check the instance attribute of a


b.show() # This is show that class programmer holds the method of Employee also so we can use it by the object of programmer
# b.showLanguage()
