marks = []

m1 = int(input("Enter the marks: "))
marks.append(m1)
m2 = int(input("Enter the marks: "))
marks.append(m2)
m3 = int(input("Enter the marks: "))
marks.append(m3)
m4 = int(input("Enter the marks: "))
marks.append(m4)
m5 = int(input("Enter the marks: "))
marks.append(m5)
m6 = int(input("Enter the marks: "))
marks.append(m6)

marks.sort()
print("Sorted marks:", marks)


# Another way to do the same thing

# marks = []

# for i in range(6):
#     mark = int(input(f"Enter marks for student {i+1}: "))
#     marks.append(mark)

# marks.sort()
# print("Sorted marks:", marks)
