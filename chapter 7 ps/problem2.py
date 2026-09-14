l = ["Harry", "Soham", "Sachin", "Rahul"] 



for i in range(0,len(l)):
    if l[i]=="Soham":
        print("Good morning ", l[i])


for i in range(0,len(l)):
    if l[i]=="Sachin":
        print("Good morning ", l[i])

    # else:
    #     print("Nothing was found")

print(l[0])



# Another way to do this problem 
# l = ["Harry", "Soham", "Sachin", "Rahul"] 

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")