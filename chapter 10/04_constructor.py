class Employee:
    language = "python" 
    salary = 1200000
    # name = "     "

    def __init__(self, name, language, salary): # dunder method which is automatically called
        self.language = language
        # self.name = name # In this case the name is accessed by the object created, otherwise by the class
        self.salary = salary
        print("I am getting the information.")


    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}") 
    @staticmethod  
    def greet():
        print("Good morning!")

harry = Employee("Aashish", "javascript", 12523652)
harry.name = "Rohan"
# harry.language = "javascript"
print(harry.name, harry.language, harry.salary)
harry.getInfo()
