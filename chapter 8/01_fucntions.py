
# Function definition
def avg():
    a = int(input("Enter the number 1: "))
    b = int(input("Enter the number 2: "))
    c = int(input("Enter the number 3: "))

    average = (a + b + c)/3
    print(average)
    return average

a = avg() # Function call
print("Done")
print(a)
avg()
print("Done")