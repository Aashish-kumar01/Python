def convertor(celsius):
    return ((9*celsius)/25) + 32

celsius = int(input("Enter the value of temperature: "))
c = convertor(celsius)
print(f"{round(c,2)}") # round will give the output upto 2 digits after decimial




# Another way to do this method
# def f_to_c():
#     return 5*(f-32)/9

# f = int(input("Enter the temperature: "))
# print(f_to_c())