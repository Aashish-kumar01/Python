import random

def game():
    print("You are playing a game")
    score = random.randint(1,12137)
    # Fetching the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print(f"Your score {score}")
    if (score<hiscore):
        print(f"Hiscore is {hiscore}")
    else:
        print("You made a New Hiscore")
    # comparing the score with hiscore
    if (score>hiscore):
        # Write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    # return score


game()
# a = game()
# print(a)