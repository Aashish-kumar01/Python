def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
    
n = int(input("Ener the number: "))

table(n)
print(f"{table(n)}")