a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if (b == 0):
    raise ZeroDivisionError("Hey are program is not meant to divide by zero")
else:
    print(f"The division of number is {a/b}")