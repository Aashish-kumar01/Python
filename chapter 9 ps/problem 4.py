
def updateword():
    with open("prb4.txt") as f:
        word = f.read()

    wordNew = word.replace("Donkeys", "#######")
    with open("prb4.txt", "w") as f:
            f.write(wordNew)


updateword()





# This problem can be done by this
# word = "Donkeys"

# with open("prb4.txt") as f:
#     content = f.read()
# contentNew = content.replace("Donkeys", "######")

# with open("prb4.txt", "w") as f:
#     f.write(contentNew)


