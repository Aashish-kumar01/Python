class Employee:
    language = "python" # This is class attributes
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}") # Here is self refers to harry which is instance of the class
    @staticmethod  
    def greet():
        print("Good morning!")

harry = Employee()
# harry.language = "Javascript" # This is instance attributes

harry.greet()
harry.getInfo() # Acutally this convert to Employee.getInfo(harry) which takes an argument harry so for this we have to give an argument in the function