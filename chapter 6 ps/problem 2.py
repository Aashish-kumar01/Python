maths = int(input("Enter your marks in maths: "))
science = int(input("Enter your marks in science: "))
english = int(input("Enter your marks in english: "))

mathspass = (maths/100)*100
sciencepass = (science/100)*100
englishpass = (english/100)*100
total = maths + science + english 
percentage = (total/300)*100

if (mathspass>33 and sciencepass>33 and englishpass>33 and total>40):
    print("You are pass")
else:
    print("You are failed")





# Another way to do this problem 

# maths = int(input("Enter your marks in maths: "))
# science = int(input("Enter your marks in science: "))
# english = int(input("Enter your marks in english: "))

# # mathspass = (maths/100)*100
# # sciencepass = (science/100)*100
# # englishpass = (english/100)*100
# total_percentage = (100*(maths + science + english))/300

# if (maths>33 and science>33 and english>33 and total_percentage>40):
#     print("You are pass")
# else:
#     print("You are failed")
