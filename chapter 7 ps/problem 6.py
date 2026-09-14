a = int(input("Enter a number: "))

fact = 1
for i in range(1,a+1):
    fact = fact*i
    i +=1

print(f"The factorial of {a} is {fact}")