import random



computer = random.choice([1,-1,0])
youstr = input("Enter you choice: ")

youDict = {"s":1, "w": -1, "g":0}
reverseDict = {1:"snake", -1:"Water", 0:"gun"}
you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if computer == you:
    print("It's a Draw")
else:
    if you == 1 and computer == -1:
        print("You Win!")
    elif you == 1 and computer == 0:
        print("You lose")
    elif you == -1 and computer == 0:
        print("You Win!")
    elif you == -1 and computer == 1:
        print("You lose")
    elif you == 0 and computer == 1:
        print("You Win!")
    elif you == 0 and computer == -1:
        print("You lose")
    else:
        print("Something went wrong!")












