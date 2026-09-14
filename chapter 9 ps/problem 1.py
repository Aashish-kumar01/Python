f = open("poem.txt")
content = f.read()
if ("Twinkle" in content):
    print("Twinkle is present in the poem")
else:
    print("Twinkle is not present in the poem")

f.close()