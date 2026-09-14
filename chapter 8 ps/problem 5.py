'''
*** 
**               
* 
'''


# def pattern(i):
#     if i==n:
#         print("*"*n)
#     return ("*"*n-1 + pattern(n-2))
    
# a = pattern(n)
# print(a)




def pattern(n):
    if n==0:
        return
    print("*"*n)
    pattern(n-1)


n = int(input("Enter a number: "))
pattern(n)

