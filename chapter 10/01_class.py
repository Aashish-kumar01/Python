class Employee:
    name = "Aashish" # This is class attributes
    language = "python"
    salary = 1200000

harry = Employee()
# harry.name = "Abhishek"  # This is instance attributes
# harry.language = "Javascript" # This is instance attributes
print(harry.name, harry.language, harry.salary)


rohan = Employee()
rohan.name = "Rohan"
rohan.language = "Java"
rohan.salary = 234426
print(rohan.name, rohan.salary, rohan.language)

