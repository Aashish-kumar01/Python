a = int(input("Enter your age: "))

# It is if elif else ladder 
if (a>=18):
    print("You are an adult")
    print("Good for you")

elif (a<0):
    print("You have enter negative age which is not a valid age")

elif (a==0):
    print("You have enter zero which is not a valid age")

else:
    print("You are a minor")

print("End the program")