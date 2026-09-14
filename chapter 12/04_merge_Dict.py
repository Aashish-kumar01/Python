dict1 = {"Aashish": 1, "Anup": 2, "Rahul": 3, "Ritik": 4}
dict2 = {5: "Akash", 6: "Abhay", 7: "Anish"}

merged = dict1 | dict2
print(merged)

# We can open multiple files using 'with' and we can read and write also
# with (
#     open("file1.txt") as f1,
#     open("file2.txt") as f2
# ):
#     content = f1.read()
#     content2 = f2.read()
#     print(content)
#     print(content2)
    