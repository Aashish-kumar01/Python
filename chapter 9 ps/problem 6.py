with open("log.txt") as f:
    word = f.read()
if ("python" in word):
    print("Pyton is present in content.") 
else:
     print("Python is not present in content.")

