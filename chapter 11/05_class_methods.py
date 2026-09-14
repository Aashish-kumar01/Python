class demo:
    name = "Aashish"
    course = "Btech"
    year = 4
    @classmethod
    def getinfo(cls):
        print(f"The name is {cls.name} who is studying the course {cls.course} whose duration is {cls.year} year")

    def getInfo(self):
        print(f"The name is {self.name} who is studying the course {self.course} whose duration is {self.year} year")



o = demo()
o.name = "Rohan"
o.course = "BSc."

o.getinfo() # here the class attribute is used over instance attribute due to @classmethod

o.getInfo() # Here the @classmethod is not used so the instance attribute is used over class attribute by default