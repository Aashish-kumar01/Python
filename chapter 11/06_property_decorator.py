class demo:
    # name = "Aashish"
    course = "Btech"
    year = 4
    # @classmethod
    def getinfo(cls):
        print(f"The name is {cls.name} who is studying the course {cls.course} whose duration is {cls.year} year")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = demo()
e.name = "Aashish Kumar"
e.getinfo()
print(e.fname)
print(e.lname)












# This shows the way to apply the property to the class
# class Student:
#     def __init__(self, name, marks):
#         self._name = name
#         self._marks = marks   # underscore means "private" by convention

#     @property
#     def marks(self):
#         return self._marks

# s = Student("Aarav", 90)
# print(s.marks)   # looks like attribute, but actually calls marks()




# This shows how to apply setter, property, deleter
# class Student:
#     def __init__(self, name, marks):
#         self._name = name
#         self._marks = marks

#     @property
#     def marks(self):
#         return self._marks

#     @marks.setter
#     def marks(self, value):
#         if value < 0:
#             raise ValueError("Marks cannot be negative")
#         self._marks = value

#     @marks.deleter
#     def marks(self):
#         del self._marks

# s = Student("Aarav", 90)
# s.marks = 95    # calls setter

# # del s.marks
# print(s.marks)