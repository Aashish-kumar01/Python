class Employee:
    company = "ITC"
    name = "Aashish"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")


class coder:
    language = "Javascript"
    name = "Rohan"
    def printlanguage(self):
        print(f"The language is {self.language}")


class programmer(Employee, coder):
    company = "ITC Infotech"
    name = "Abhishek"
    language = "Python"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


# a = Employee()
b = programmer()
# a.show()
b.show()
b.showLanguage()
b.printlanguage()
