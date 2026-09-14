'''
sum(1) = 1
sum(2) = 3
sum(3) = 6
sum(4) = 10
sum(n) = 1 + 2 + 3 + 4 + ..... + n
sum(n) = n*(n-1)/2
sum(n) = n**2/2 - n/2
'''






def sum(n):
    if n==1:
        return 1
    return (n + sum(n-1))
    # for i in range(1,n):
    
n = int(input("Enter the number: "))  
print(sum(n))
