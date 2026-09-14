

# import os

# if os.path.exists("log.txt"):
#     print("File is exists")

# else:
#     print("File is not exists")




# Another way to do this method
# from pathlib import Path

# file_path = Path("hiscore.txt")

# if file_path.is_file():
#     print("File is exists ")


# else:
#     print("file is not exists")





# This is a method of doing the same thing using with statement
with open("this.txt") as f: 
    content1 = f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("Yes these files are identicals")
else:
    print("No these files are not identicals")




