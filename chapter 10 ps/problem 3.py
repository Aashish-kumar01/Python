
# Yes the instance attributes will be more priorities over class attribute
class attribute:
    a = 17

object = attribute()
print(object.a) # for this time instance attribute is not available so this print the class attrbute
object.a = 0
print(object.a) # Now the instance attribute is available so it prints the instance atribute
print(attribute.a) # The instance attribute will not change the class attribute so it prints the class attribute